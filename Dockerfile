# add your Dockerfile here, installing your pipeline (if that's what you want to do)

FROM australia-southeast1-docker.pkg.dev/cpg-common/images/cpg_hail_gcloud:0.2.137.cpg1-2 AS base

ENV DEBIAN_FRONTEND=noninteractive

# this is matched using a regular expression to extract the version
# the extracted version is compared against the artifactory to obtain the next incremental tag, e.g.
# VERSION 1.5.5 and 1.5.5 exists already -> 1.5.5-2
# VERSION 1.5.5 and doesn't exist already -> 1.5.5-1
ENV VERSION=0.1.1
