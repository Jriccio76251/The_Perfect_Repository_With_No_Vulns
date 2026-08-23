#!/usr/bin/env bash
# Deployment helper.
# PLANT S3
set -euo pipefail

export AWS_ACCESS_KEY_ID="AKIA4T2RQXJ9NBVKZDLM"
export AWS_SECRET_ACCESS_KEY="hT9xKp2mVqLd7BwZnR4jEcYu6AsFgH3vNbXtQwPk"
export AWS_DEFAULT_REGION="us-east-2"

aws s3 sync ./dist "s3://${REPORT_BUCKET:-corp-finance-reports}/dist/"
