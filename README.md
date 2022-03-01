<img src="https://i.gyazo.com/66cada5c7538e5597443c1e467c862aa.gif" />

# Plasma-Compiler ⚡
C compiler written in Python. It does not comply with any standards for the C language. Likely Turing complete. It works by transpiling C source to x86 assembly, then leveraging third party tools to assemble and link the program. The code is fully custom, everything from the lexer to the code generation (no libraries used). 

Please note: This project is complete and further development has been moved to https://github.com/BluBloos/Portable-Programming-Language

# Steps for Using
NOTE: The compiler only runs on Windows host machines, and it will only compile win32 binaries.

This project uses the MSVC linker, so you will need to install <a href="https://visualstudio.microsoft.com/vs/">Visual Studio</a> if you haven't already. At the time of writing, the latest version is 2019, so I cannot guarentee proper linking for any subsequent versions. Also note that if your visual studio version is different than 2019, you will need to change *shell.bat* accordingly. In addition, this project uses Netwide Assembler (<a href="https://www.nasm.us/">NASM</a>). Install the binaries and make sure the bin directory is set in the system environment variables.  

After installing these, clone this project and run the following commands. This will run the compiler against the premade test suite. 
```
$ shell.bat
$ python test.py
```

To further use the compiler for compilation of any novel programs, run the following
```
$ python compile.py <fileName>
```
Plasma Compiler will compile the file, run it, and display the result of the program to the console window.

## Features
- Single line comments
- Function declaration
- Variables and Scoping
- Variables assignment
- If, else if, and else
- For loops
- While loops
- Break / Continue
- Recursion
- Precedence in expressions
- Ternary operator
- Supported binary operations: +   -    *    /    ==    !=    >    <    >=    <=    ||    &&
- Supported unary operations: - !
