import time
BEGIN = time.time()

import logger
import lexer
import syntax
import semantics
import codegen
import optimization
import argparse
from colorama import init
from colorama import Fore, Back, Style

import sys
import os
import subprocess

def Run(fileName, DEBUG, TEST, platform):

    file = open(fileName, "r")
    raw = file.read()

    #TODO(Noah): What happens if the file read fails?
    file.close()

    tokens = lexer.Run(raw)

    if DEBUG:
        for token in tokens.tokens:
            logger.Log("TYPE: " + token.type + ", VALUE: " + token.value)

    tree = syntax.Run(tokens, logger)

    if not tree:
        sys.exit()

    if DEBUG:
        tree.Print(0)
        #tree.PrintWeights(0)
        #print("Depth: " + str(tree.depth))

    #annotatedTree, result = semantics.Run(tree, logger)

    #if result == False:
    #    sys.exit()
    file = open(fileName + ".asm", "w")
    codegen.Run(platform, tree, file)
    file.close()
    #instructions = optimization.Run(instructions)

    #TODO(Noah): There is more room for error here
    #write out assembler instructions

    # Assemble and link the code (using 3rd party software)
    exe_name = "{}.exe".format(fileName)

    if (platform == "WINDOWS"):
        subprocess.run(["nasm", "-fwin32", "{}.asm".format(fileName)])
        subprocess.run(["link", "/subsystem:console", "/entry:start" ,
                        "{}.obj".format(fileName), "/OUT:{}".format(exe_name)])
    elif (platform == "LINUX"):
        pass

    return_val = 0

    if TEST:
        if os.path.isfile(exe_name):
            if DEBUG:
                print("Running {}".format(exe_name))
            result = subprocess.run([exe_name])
            return_val = result.returncode
            if DEBUG:
                print("Return Code: {}".format(result.returncode))

    END = time.time()
    ELAPSED = round((END - BEGIN) * 1000, 3)
    logger.Log("Elapsed: " + str(ELAPSED) + "ms")

    return return_val

def colored(string, color):
    if color == "green":
        return Fore.GREEN + string
    elif color == "red":
        return Fore.RED + string

def SingleTest(fileName, desired_result):
    global PLATFORM
    debug = False
    test = True
    result = Run(fileName, debug, test, PLATFORM)
    if desired_result == result:
        print(colored("{} works.".format(fileName), "green"))
        print(Style.RESET_ALL)
    else:
        print(colored("Error: {} does not work.".format(fileName), "red"))
        print(Style.RESET_ALL)

def RunAllTests():

    global PLATFORM
    init()
    PLATFORM = "WINDOWS"

    SingleTest("tests/variable_scoping.c", 3)
    SingleTest("tests/variables.c", 5)
    SingleTest("tests/expression.c", 1)
    SingleTest("tests/comments.c", 0)
    SingleTest("tests/function.c", 65)
    SingleTest("tests/function2.c", 128)
    SingleTest("tests/factorial.c", 6)
    SingleTest("tests/if.c", 100)
    SingleTest("tests/if2.c", 80)
    SingleTest("tests/if3.c", 40)
    SingleTest("tests/conditional.c", 12)
    SingleTest("tests/fib.c", 13)
    SingleTest("tests/for.c", 5)
    SingleTest("tests/while.c", 10)

 
if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog='Plasma Compiler',
        description='Compile C programs.')
    parser.add_argument('filename', nargs='?', help="The file to process.", default=None)
    parser.add_argument('-d', '--debug', action='store_true', help="Enable debug mode.")
    parser.add_argument('-r', '--run', action='store_true', help="Run code after compile.")
    parser.add_argument('-t', '--test', action='store_true', help="Run all tests (ignores positional argument).")
    args = parser.parse_args()

    if args.test:
        RunAllTests()
    else:
        if args.filename is not None:
            platform = "WINDOWS"
            DEBUG = args.debug
            Run(args.filename, DEBUG, args.run, platform)
        else:
            logger.Error("No source file.")