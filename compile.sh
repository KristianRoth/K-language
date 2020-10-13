#!/bin/bash
nasm -f macho64 hellomac.asm && ld -macosx_version_min 10.7.0 -lSystem -o hellomac hellomac.o && ./hellomac