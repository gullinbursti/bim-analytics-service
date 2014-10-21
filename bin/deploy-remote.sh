#! /bin/bash

set -o xtrace
set -o errexit
set -o pipefail

export DJANGO_SETTINGS_MODULE='bimanalytics.settings'
export BIMANALYTICS_CONFIG_DIR='/etc/bimanalytics'

build_id="$(date +%Y%m%d%H%M%S)-${SVN_URL:-MANUAL_BUILD}"
dist_dir="dist-$build_id"
link_path='/opt/built-in-menlo/bimanalytics'

# Absolute path critical for honoring virtualenv in `pip_cmd` and
# `django_admin_cmd`
install_dir="/opt/built-in-menlo/versions/bimanalytics-$build_id"
pip_cmd="$install_dir/bin/pip"
django_admin_cmd="$install_dir/bin/django-admin.py"

echo ""
echo "-------------------------------------------------------------------------------"
echo "- Building: $build_id"
echo "-------------------------------------------------------------------------------"
# The following can be done outside of a virtualenv
mkdir "$dist_dir"  # We want the build to fail if `dist_dir` exists!!!
./setup.py sdist --dist-dir "$dist_dir"
package_path=$(ls -1 $dist_dir/bimanalytics-*.tar.gz | sort -u | tail -1)

echo ""
echo "-------------------------------------------------------------------------------"
echo "- Deploying: $install_dir"
echo "-------------------------------------------------------------------------------"
mkdir -p "$install_dir"
virtualenv --python=python2.7 "$install_dir"
"$pip_cmd" install -U pip
"$pip_cmd" install "$package_path"
(cd "$install_dir" && "$django_admin_cmd" collectstatic --noinput)
ln -fsnv "$install_dir" "$link_path"
sudo /usr/sbin/service apache2 restart
