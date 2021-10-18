# nand2tetris:Project0:removeBlankAndComment.py

Author: Sun Luzhe

Time:2021.10.11

## 1.Purpose of this program

This is a program to remove white space and comments from a text file and then create a output file in the same directory named <filename>.out

In details:

1) Remove white space:
   Strip out all white space from <filename>.in. White space in this case means spaces, tabs, and blank lines, but not line returns.
2) Remove comments:
   Remove all comments in addition to the whitespace. Comments come in two forms:
   1.comments begin with the sequence "//" and end at the line return
   2.comments begin with the sequence /* and end at the sequence */

## 2.How to compile and run

step1: open terminal

step2: input

```
python <path of this program> <path of targetfile>
```

- The filename and program name can be an absolute or a relative file path, choose as you like.
- <font color='red'>Attention: We assume all the target name in format "filename.in". If you want to change it to any other format like "filename.txt", you need make some change in the code, but it is very simple. </font>

## 3.Environment requirement

To run this program, your computer need to install python3

## 4.Input sample and output sample

Input: testfile.in

```assembly
/* Draws a rectangle at the top-left corner of the screen.
The rectangle is 16 pixels wide and R0 pixels high. */

(KBDLOOP)
    @KBD   //loop until key pressed
    D=M
    @KBDLOOP
    D;JEQ

    @50    //setup: rect will be 50 high
    D=A
    @R0
```

Output: testfile.out

```assembly
(KBDLOOP)
@KBD
D=M
@KBDLOOP
D;JEQ
@50
D=A
@R0
```

## 5.Test results

The program can work correctly in both terminal and IDE. See how to switch to IDE in 6.5.

## 6.Main structure of this program

(If you do not care, feel free to skip this part. It is not necessaary for users.)

The program consist of 6 functions:

#### 1.remove_singleline_comment

```python
def remove_singleline_comment(lines, i):
    '''
    This function is aim to remove comment like "//......" in file lines

    :param lines: list : lines read from the file
    :param i: int : current line index
    :return: None
    '''
```

#### 2.remove_multiline_comment

```python
def remove_multiline_comment(lines, i):
    '''
    This function is aim to remove comment like "/*......*/" in file lines

    :param lines: list : lines read from the file
    :param i: int : current line index
    :return: int : 0 : Not find comment
                  -1 : comment line between "/*" and "*/", remove
                  -2 : Only find "/*" in this line
    '''
```

#### 3.remove_comment_from_file

```python
def remove_comment_from_file(file_name):
    '''
    This program can remove white space and comments from the file
    :param file_name: string : input file name
    :return: lines : list : the file content after process
    '''
```

#### 4.write_result

```python
def write_result(filename, lines):
    '''
    This function can create a output file which store the result
    :param filename: string: output file name
    :param lines: list
    :return: none
    '''
```

#### 5.output_result

Declare: This function is not necessary, just for test in IDE to check result so I comment it in the main function

```python
def output_result(result):
    '''
    This function can print the result in the console, so the programmer can check the    result
    :param result: list
    :return: None
    '''
```

#### 6.Main

In this part, you have two choices:

1) Run in terminal

2) Run in IDE

Feel free to choose what you like

```python
if __name__ == '__main__':    # Run for terminal    .....    # if you want to test in IDE uncomment the below and comment the above in main function    '''    ......    '''
```

