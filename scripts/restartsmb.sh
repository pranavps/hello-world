#!/bin/bash
set -eux

systemctl restart smb.service
systemctl restart nmb.service

set +eux
