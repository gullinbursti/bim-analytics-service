#! /bin/bash

# This script is used by `deploy-jenkins.sh` on the server being deployed to.

set -o xtrace
set -o errexit
set -o pipefail
set -o nounset

export DJANGO_SETTINGS_MODULE='bimanalytics.settings'
export BIMANALYTICS_CONFIG_DIR='/home/bim-deploy/.bim-build-conf'

service_type="$1"
build_id="$2"
package_path="$3"
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

case "$service_type" in
    'apache')
        sudo /usr/sbin/service apache2 restart
        ;;
    'celery')
        sudo /usr/sbin/service celeryd-bimanalytics restart
        ;;
    *)
        echo "ERROR - Unknown service_type: $service_type"
        exit 1
        ;;
esac

