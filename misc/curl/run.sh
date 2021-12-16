#!/bin/bash

docker run -it --read-only -p2222:22 --cap-add cap_dac_read_search curl
