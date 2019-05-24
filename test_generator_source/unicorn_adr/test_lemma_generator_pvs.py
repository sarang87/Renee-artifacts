#!/usr/bin/env python
# Run the script using python test_lemma_generator_pvs.py <<ASL_inst.xml>> <<ASL_inst_class_name>>
# For example, python test_lemma_generator_pvs.py subs_addsub_shift.xml addsub_shift


import xml.etree.ElementTree as ET
import sys
import json

import re
import os
import os.path as path
import pickle
import master_test as mtest
import test_concrete as tc


class pvs_lemma_generator:

    # Initializes variables for pvs_lemma_generator, input registers, output registers, bitstrings which are randomly generated by the master_test modul
    def __init__(self, pvs_filename):
        self.pvs_lemma_filename = pvs_filename
        # extract the class name from the file name
        self.inst_class = self.pvs_lemma_filename.rsplit("_", 1)[0]
        self.name_inputfile = ""
        self.cur_dir = os.path.abspath('')
        self.unicorn_file_dir = cur_dir + "/unicorn_outputs/"
        self.f = open(self.unicorn_file_dir + pvs_lemma_filename + ".pvs", "w")
        self.input_bitstring = ""
        self.input_hexstring = ""
        self.Rd = ""
        self.Rn = ""
        self.Rm = ""

        # These store the initial values when running the instruction on Unicorn
        self.Rd_val = []
        self.Rn_val = []
        self.Rm_val = []
        self.R_NZCV = []
        self.R_PC = []

        # This stores the register number of the output register in Unicorn
        self.R_op = ""
        self.R_op_val = ""

    # This generates the PVS lemma file for the corresponding Unicorn output file for a randomly generated instruction that respects the instruction format
    def generate_pvs_lemma_file(self):
        self.f.write(self.pvs_lemma_filename)
        self.f.write(" : THEORY\n")
        self.f.write("\n      BEGIN\n")
        self.f.write("\n      IMPORTING rsl@adr\n")

        self.f.write("\n      X_sts : [ below(32) -> bvec[64] ] = init`X with [( " + self.Rd + " ) := " + self.Rd_val[0] + "] \n") # + "\n\t\t\t\t\t\t\t ( " + self.Rn + " ):= " + self.Rn_val[0] + "," + "\n\t\t\t\t\t\t\t ( " + self.Rm + " ):= " + self.Rm_val[0] + "] \n")
        
        self.f.write(
            "\n      p     : s = init with [`X := X_sts, `PC := (# b := bv[64](0b" + self.pad_PC_with_zeroes(self.R_PC[0]) + "), i := " + self.R_PC[0] + " #)]\n")
        self.f.write("\n      adr_1 : Theory = adr[p]{{ Diag := bv(0b" + self.input_bitstring + ") , addr := " + self.R_PC[0] + "}}\n")

        self.f.write(
            "\n      test1 : lemma let X_post = p`X with [ ( " + self.Rd + " ) " + ":= " + self.R_op_val + "] in\n")
        self.f.write(
            "\n                    let p2     = p with [`X := X_post] in \n") #% `NZVC:= " + self.R_NZCV[1] + " , `PC:= " + self.R_PC[1] + "] in\n")
        self.f.write("\n                                 adr_1.post`X( " + self.Rd + " ) = p2`X( " + self.Rd + " )\n")
        
        self.f.write("\n%|- X_sts_TCC* : PROOF")
        self.f.write("\n%|- p_TCC1     : PROOF")
        self.f.write("\n%|- adr_1_TCC* : PROOF")
        self.f.write("\n%|- test1_TCC1 : PROOF (eval-formula)")
        self.f.write("\n%|- QED\n")

        self.f.write("\n%|- test1 : PROOF ( pc-related-addr )")
        self.f.write("\n%|- QED\n")
        self.f.write("\nEND " + self.pvs_lemma_filename)

    def pad_PC_with_zeroes(self, pc):
        bin_pc = bin(int(pc))
        result = bin_pc[2:][::-1].ljust(64, '0')
        return result
    
    # This method sets the filename for the unicorn_output_file which is the input file for this program to generate the pvs test lemma file
    def set_name_inputfile(self, filename):
        self.name_inputfile = filename

    # This method reads from the output file generated by Unicorn for an instruction simulation to extract the parameter values ofr pvs lemma file
    def parse_unicorn_output_file(self):
        try:
            unicorn_file_ptr = open(
                self.unicorn_file_dir + self.name_inputfile, "r")
            print "Opening file " + self.name_inputfile
            for line in unicorn_file_ptr:
                line = line.strip()
                if "=" in line:
                    tokens = line.split("=")
                    if tokens[0] == "input_bitstring":
                        self.input_bitstring = tokens[1]
                    elif tokens[0] == "input_hexstring":
                        self.input_hexstring = tokens[1]
                    elif tokens[0] == "Rd":
                        self.Rd = tokens[1]
                    # elif tokens[0] == "Rn":
                        # self.Rn = tokens[1]
                    # elif tokens[0] == "Rm":
                        # self.Rm = tokens[1]
                    elif tokens[0] == "Rd_pre":
                        self.Rd_val.append(tokens[1])
                    # elif tokens[0] == "Rn_pre":
                        # self.Rn_val.append(tokens[1])
                    # elif tokens[0] == "Rm_pre":
                        # self.Rm_val.append(tokens[1])
                    elif tokens[0] == "R_PC_pre":
                        self.R_PC.append(tokens[1])
                    # elif tokens[0] == "R_NZCV_pre":
                        # self.R_NZCV.append(tokens[1])
                    elif tokens[0] == "Rd_post":
                        self.Rd_val.append(tokens[1])
                    # elif tokens[0] == "Rm_post":
                        # self.Rm_val.append(tokens[1])
                    # elif tokens[0] == "Rn_post":
                        # self.Rn_val.append(tokens[1])
                    elif tokens[0] == "R_PC_post":
                        self.R_PC.append(tokens[1])
                    # elif tokens[0] == "R_NZCV_post":
                        # self.R_NZCV.append(tokens[1])
                    elif tokens[0] == "R_op":
                        self.R_op = tokens[1]
                    elif tokens[0] == "R_op_val":
                        self.R_op_val = tokens[1]
        except IOError:
            print "Error: File does not appear to exist."
            return 0


if __name__ == '__main__':
    cur_dir = os.path.abspath('')
    output_dir = cur_dir + "/unicorn_outputs/"
    # argv[1] is the name of the instruction which needs to be randomly generated and tested
    inst_filename = sys.argv[1]
    # initialize the values for NZCV register from here
    # nzcv_list = [0xF0000000, 0xE0000000, 0xD0000000, 0xC0000000, 0xB0000000, 0xA0000000, 0x90000000, 0x80000000,
                #  0x70000000, 0x60000000, 0x50000000, 0x40000000, 0x30000000, 0x20000000, 0x10000000, 0xE0000000]
    # for item in nzcv_list:
        # Remove the ".xml" from the arg to get the instruction name
    inst_name = inst_filename.replace(".xml", "")
    # Create an object of the inst_generator class
    inst_test_suite = mtest.inst_generator(inst_filename)
    # Extracts the diagram format from ASL for each instruction which is provided in the command line as an argument
    inst_test_suite.extract_fields()
    # Generates a txt file with field names about the random bitstring generated for a particular ARM inst
    inst_test_suite.generate_validation_file()
    # Extract registers from the previous output
    reg_list = inst_test_suite.get_registers()
    # Fixes the bytestring issue in unicorn for the test genration
    int_list = inst_test_suite.get_bytestr()
    bytecode = bytearray(int_list)
    # Unicorn output file
    unicorn_output_file_name = inst_test_suite.get_hexstring()
    op_fileptr = open(output_dir + unicorn_output_file_name, "w")
    bitstring = inst_test_suite.get_pvs_bitstring()
    hexstring = unicorn_output_file_name
    # Add more info to the file for repeating the test case using the bitstring, hexstring , int_list combination
    op_fileptr.write("input_bitstring=" + bitstring + "\n")
    op_fileptr.write("input_hexstring=" + hexstring + "\n")
    op_fileptr.write("reg_list=" + str(reg_list) + "\n")
    op_fileptr.write("int_list=" + str(int_list) + "\n")
    # Run the instruction
    mtest.test_arm64(bytes(bytecode), op_fileptr, reg_list)
    # Code for generating the pvs lemma file from the unicorn output file
    pvs_lemma_filename = inst_name + "_" + unicorn_output_file_name
    pvs_lemma_filename = pvs_lemma_filename.upper()
    pg = pvs_lemma_generator(pvs_lemma_filename)
    # This sets the name of the inout file for pvs lemma generator to the output file generated by unicorn
    pg.set_name_inputfile(unicorn_output_file_name)
    pg.parse_unicorn_output_file()
    pg.generate_pvs_lemma_file()
    print "Generating " + pvs_lemma_filename + ".pvs"
    generate_pvs = tc.test_concrete(bitstring, hexstring)

    #############################################################

        #Decupling the concrete file generation logic from the pvs file generation logic.

    #############################################################
    # print "Generating the test_concrete file for the instruction"
    # generate_pvs.extract_inst_class()
    # generate_pvs.extract_theory_parameters()
    # inst_imm.view_fields()
    # generate_pvs.generate_pvs_code()
