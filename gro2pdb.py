#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Program to convert .gro to .pdb
"""

import sys, signal
sys.dont_write_bytecode = True
signal.signal(signal.SIGINT, signal.SIG_DFL)

import argparse
import os
import parmed



# =============== main =============== #
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Program to convert .gro to .pdb", formatter_class=argparse.RawTextHelpFormatter)
	parser.add_argument("-i", dest="INPUT_GRO", metavar="INPUT.gro", required=True, help="source .gro file")
	parser.add_argument("-o", dest="OUTPUT_PDB", metavar="OUTPUT.pdb", required=True, help="output .pdb file")
	parser.add_argument("-O", dest="FLAG_OVERWRITE", action="store_true", default=False, help="overwrite forcibly")
	args = parser.parse_args()

	if not os.path.isfile(args.INPUT_GRO):
		sys.stderr.write("ERROR: No such file `{}`.\n".format(args.INPUT_GRO))
		sys.exit(1)

	obj_mol = parmed.load_file(args.INPUT_GRO)

	if os.path.isfile(args.OUTPUT_PDB):
		if args.FLAG_OVERWRITE == False:
			sys.stderr.write("WARNING: `{}` already exists. Do you want to overwrite it? (y/N) > ".format(args.OUTPUT_PDB))
			sys.stderr.flush()
			user_choice = sys.stdin.readline().strip()
			if user_choice not in ["y", "Y"]:
				sys.exit(0)

		os.remove(args.OUTPUT_PDB)

	obj_mol.save(args.OUTPUT_PDB)
