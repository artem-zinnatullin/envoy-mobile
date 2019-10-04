#!/usr/bin/env python

from __future__ import print_function

import os

import argparse
import shutil

try:
    from urllib.request import urlopen, Request, HTTPError
except ImportError:  # python 2
    from urllib2 import urlopen, Request, HTTPError

_ARTIFACT_SERVER_USER = os.environ.get("ARTIFACT_SERVER_USER", "")
_ARTIFACT_SERVER_PASS = os.environ.get("ARTIFACT_SERVER_PASS", "")
_ARTIFACT_SERVER_URL = os.environ.get("ARTIFACT_SERVER_URL", "")

_MAVEN_GROUP_ID = "io.envoyproxy.envoymobile"
_MAVEN_ARTIFACT_ID = "envoy-mobile"
_BASE_URL = "{}/io/envoyproxy/envoymobile".format(_ARTIFACT_SERVER_URL)

_LOCAL_INSTALL_PATH = os.path.expanduser("~/.m2/repository/io/envoyproxy/envoymobile/{}".format(_MAVEN_ARTIFACT_ID))


# TODO remove
def dump(obj):
    for attr in dir(obj):
        print("obj.%s = %r" % (attr, getattr(obj, attr)))


def prepare_files_for_deploy(tmp_dir, artifact_version):
    pom = "{dir}/{artifact_id}-{version}.pom".format(dir=tmp_dir, artifact_id=_MAVEN_ARTIFACT_ID,
                                                     version=artifact_version)
    shutil.copy("dist/envoy-mobile-pom.xml", pom)

    aar = "{dir}/{artifact_id}-{version}.aar".format(dir=tmp_dir, artifact_id=_MAVEN_ARTIFACT_ID,
                                                     version=artifact_version)
    shutil.copy("dist/envoy-mobile.aar", aar)

    javadocJar = "{dir}/{artifact_id}-{version}-javadoc.jar".format(dir=tmp_dir, artifact_id=_MAVEN_ARTIFACT_ID,
                                                                    version=artifact_version)
    shutil.copy("dist/envoy-mobile-javadoc.jar", javadocJar)

    sourcesJar = "{dir}/{artifact_id}-{version}-sources.jar".format(dir=tmp_dir, artifact_id=_MAVEN_ARTIFACT_ID,
                                                                    version=artifact_version)
    shutil.copy("dist/envoy-mobile-sources.jar", sourcesJar)

    return [
        pom,
        aar,
        javadocJar,
        sourcesJar
    ]


# Returns list of signed files (.asc).
def gpg_sign_files(files):
    return files


def deploy_to_maven_server(files):
    None


def deploy_to_maven_local(files):
    None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifact-version", type=str)
    parser.add_argument('--sign', type=bool)
    parser.add_argument('--deploy-to-maven-server', type=bool)
    parser.add_argument('--deploy-to-maven-local', type=bool)
    parser.add_argument("--tmp-dir", type=str)
    args = parser.parse_args()

    files = prepare_files_for_deploy(args.tmp_dir, args.artifact_version)

    print("Found files for deploy: {}".format(files))

    if args.sign:
        print("Signing files: {}".format(files))
        files = files + gpg_sign_files(files)

    if args.deploy_to_maven_local:
        print("Deploying files to maven local: {}".format(files))
        deploy_to_maven_local(files)

    if args.deploy_to_maven_server:
        print("Deploying files to maven server: {}, {}".format(_ARTIFACT_SERVER_URL, files))
        deploy_to_maven_server(files)

    print("maven_deploy has finished.")


if __name__ == "__main__":
    main()
