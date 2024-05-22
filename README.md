# Plasma-Compiler ⚡

C compiler written in Python. It does not comply with any standards for the C
language. Likely Turing complete. It works by transpiling C source to x86
assembly, then leveraging third party tools to assemble and link the program.
The code is fully custom, everything from the lexer to the code generation (no
libraries used).

> NOTE: This project was developed when I was in high school and therefore does
> not reflect my current expertise. I have made minor updates to the project
> since then, but the majority of the codebase remains unchanged from the
> original version.

<p align="center">
<img src="https://i.gyazo.com/66cada5c7538e5597443c1e467c862aa.gif" />
</p>

# Features

- Single line comments
- Function declaration
- Variable declaration and assignment
- Variable Scoping
- If, else if, and else
- For loops
- While loops
- Break / Continue
- Recursion
- Precedence in expressions
- Ternary operator
- Supported binary operations: +   -    *    /    ==    !=    >    <    >=    <=    ||    &&
- Supported unary operations: - !


# Steps for Using

NOTE: The compiler only runs on Windows host machines, and it will only compile
win32 binaries.

## Dependencies

This project uses the MSVC linker, so you will need to install <a
href="https://visualstudio.microsoft.com/vs/">Visual Studio</a> if you haven't
already. 
> At the time of writing, the latest version is 2019, so I cannot
guarantee proper linking for any subsequent versions. 
Also note that if your
Visual Studio version is different than 2019, you will need to change
*shell.bat* accordingly.

### Development Dependencies

If running the compiler via the .py files and a suitable Python Interpreter,
some Python dependencies must be installed,

```
pip install -r requirements.txt
```

In addition, this project uses Netwide Assembler (<a
href="https://www.nasm.us/">NASM</a>). Install the binaries and make sure the
bin directory is set in the system environment variables.  

## Setup

To use the compiler, open a new command prompt and run,

```
shell.bat
```

This will setup the MSVC environment, so that link.exe is accessible.

**The compiler will not log an error if link.exe is unavailable.**

## Normal Usage

```
usage: Plasma Compiler [-h] [-d] [-r] [-t] [filename]

positional arguments:
  filename     The file to process.

options:
  -h, --help   show this help message and exit
  -d, --debug  Enable debug mode.
  -r, --run    Run code after compile.
  -t, --test   Run all tests (ignores positional argument).
```
