#! /bin/bash

set -o xtrace
set -o errexit
set -o pipefail
set -o nounset

build_id="$1"
dist_dir="dist-$build_id"

echo ""
echo "-------------------------------------------------------------------------------"
echo "- Building: $build_id"
echo "-------------------------------------------------------------------------------"
# The following can be done outside of a virtualenv
mkdir "$dist_dir"  # We want the build to fail if `dist_dir` exists!!!
./setup.py sdist --dist-dir "$dist_dir"
package_path=$(ls -1 $dist_dir/bimanalytics-*.tar.gz | sort -u | tail -1)
