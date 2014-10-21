#! /bin/bash

# This script is used by `deploy-jenkins.sh` on the server being deployed to.

set -o xtrace
set -o errexit
set -o pipefail
set -o nounset

export DJANGO_SETTINGS_MODULE='bimanalytics.settings'
export BIMANALYTICS_CONFIG_DIR='/etc/bimanalytics'

build_id="$1"
package_path="$2"
link_path='/opt/built-in-menlo/bimanalytics'


echo ""
echo "-------------------------------------------------------------------------------"
echo "- *$(basename $0)* Deploying: $package_path ($build_id)"
echo "-------------------------------------------------------------------------------"
# Absolute path critical for honoring virtualenv in `pip_cmd` and
# `django_admin_cmd`
install_dir="/opt/built-in-menlo/versions/bimanalytics-$build_id"
pip_cmd="$install_dir/bin/pip"
django_admin_cmd="$install_dir/bin/django-admin.py"


mkdir -p "$install_dir"
virtualenv --python=python2.7 "$install_dir"
"$pip_cmd" install -U pip
"$pip_cmd" install "$package_path"
(cd "$install_dir" && "$django_admin_cmd" collectstatic --noinput)
ln -fsnv "$install_dir" "$link_path"
sudo /usr/sbin/service apache2 restart
