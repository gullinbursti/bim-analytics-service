#! /bin/bash

# This script gets executed locally on a Jenkins server.  It:
#    1. Creates a source distribution of the Python package.
#    2. scp`s the new packagei, and `deploy-remote.sh`  to the target server
#    3. Kicks odd `./deploy-remote.sh` on the remote server to finalize the
#       installation.

set -o xtrace
set -o errexit
set -o pipefail
set -o nounset

build_id="$1"
dist_dir="dist-$build_id"

echo ""
echo "-------------------------------------------------------------------------------"
echo "- *LOCAL* Building: $build_id"
echo "-------------------------------------------------------------------------------"
# The following can be done outside of a virtualenv
mkdir "$dist_dir"  # We want the build to fail if `dist_dir` exists!!!
./setup.py sdist --dist-dir "$dist_dir"
package_path=$(ls -1 $dist_dir/bimanalytics-*.tar.gz | sort -u | tail -1)
package_name=$(basename "$package_path")

ssh_proxy='ProxyCommand ssh bim-deploy@bastion.selfieclubapp.com nc -q0 %h %p 2> /dev/null'
remote_host='bim-deploy@api00.devint.selfieclubapp.com'
remote_tmp_dir="/opt/built-in-menlo/tmp/bimanalytics/$build_id"

echo ""
echo "-------------------------------------------------------------------------------"
echo "- *LOCAL* Shipping: $build_id"
echo "-------------------------------------------------------------------------------"
ssh -o "$ssh_proxy" "$remote_host" <<EOC
    set -o xtrace
    set -o errexit
    test ! -d "$remote_tmp_dir" || exit 1
    mkdir -pv "$remote_tmp_dir"
EOC
scp -o "$ssh_proxy" "$package_path" "bin/deploy-remote.sh" "$remote_host:$remote_tmp_dir/"
ssh -o "$ssh_proxy" "$remote_host" <<EOC
    set -o xtrace
    set -o errexit
    cd "$remote_tmp_dir"
    ./deploy-remote.sh "$build_id" "$package_name"
EOC
