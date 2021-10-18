'''
Author: Sun Luzhe
Time:2021.10.11

Purpose of this program:
a program to remove white space and comments from a text file.

In details:
1) Remove white space:
Strip out all white space from <filename>.in. White space in this case means spaces, tabs, and blank lines, but not line returns.
2) Remove comments:
Remove all comments in addition to the whitespace. Comments come in two forms:
1.comments begin with the sequence "//" and end at the line return
2.comments begin with the sequence /* and end at the sequence */
'''
import sys
'''
begin_found use to mark whether program has already found the mark "/*" and is going to find "*/"
you can see how it works in below code
'''
global begin_found
begin_found = False


def remove_singleline_comment(lines, i):
    '''
    This function is aim to remove comment like "//......" in file lines

    :param lines: list : lines read from the file
    :param i: int : current line index
    :return: None
    '''

    # find whether comment in format "//..." exists
    index = lines[i].find("//")
    if index != -1:
        # remove comment
        lines[i] = lines[i][0:index]
        # remove blank
        lines[i] = lines[i].replace(' ', '').replace('\t', '')
        lines[i]+='\n'

    return


def remove_multiline_comment(lines, i):
    '''
    This function is aim to remove comment like "/*......*/" in file lines

    :param lines: list : lines read from the file
    :param i: int : current line index
    :return: int : 0 : Not find comment
                  -1 : comment line between "/*" and "*/", remove
                  -2 : Only find "/*" in this line
    '''

    # begin_found use to mark whether program has already found the mark "/*" and is going to find "*/"
    global begin_found

    while True:
        if not begin_found:
            # go find "/*"
            index_begin = lines[i].find("/*")

            # if find "/*" set begin_found true
            if index_begin != -1:
                begin_found = True

                # go find "*/" in the same line
                index_end = lines[i].find("*/", index_begin + 2)

                # if find "*/" in the same line remove the line and set begin_found false
                if index_end != -1:
                    lines[i] = lines[i].replace(lines[i], '')
                    begin_found = False  # continue find comment

                # Do not find "*/" in the same line, just remove the line
                else:
                    lines[i] = lines[i].replace(lines[i], '')
                    lines[i]+=''
                    return -2

            # No sign like "/*" in this line
            else:
                lines[i] = lines[i].replace(' ', '').replace('\t', '')
                return 0

        # already find "/*" but not find "*/", go find "*/"
        else:
            index_end = lines[i].find("*/")

            # if find "*/" , remove the line and set begin_found false
            if index_end != -1:
                begin_found = False
                lines[i] = lines[i].replace(lines[i], '')  # continue find comment

            # comment line between "/*" and "*/", remove
            else:
                return -1


def remove_comment_from_file(file_name):
    '''
    This program can remove white space and comments from the file
    :param file_name: string : input file name
    :return: lines : list : the file content after process
    '''
    global begin_found
    # open file and get content
    f = open(file_name)
    lines = f.readlines()
    f.close()
    length = len(lines)
    # loop lines to process comment
    i = 0
    while i < length:
        ret = remove_multiline_comment(lines, i)
        # comment line between "/*" and "*/", remove
        if ret == -1:
            if begin_found == False:
                print("There are some wrong comment sentences")
            else:
                del lines[i]
                # since we remove the line length has change
                i -= 1
                length -= 1

        # No sign like "/*" in this line
        elif ret == 0:
            remove_singleline_comment(lines, i)

        # only find "/*" in this line, function already handle others
        else:
            pass

        i += 1

    return lines

# Declare: This function is not necessary, just for test in IDE to check result so I comment it in the main function
def output_result(result):
    '''
    This function can print the result in the console, so the programmer can check the result
    :param result: list
    :return: None
    '''
    for line in result:
        if line == '' or line == '\n':
            continue
        else:
            # remove blank line
            print(line.replace('\n', ''))

    return

def write_result(filename, lines):
    '''
    This function can create a output file which store the result
    :param filename: string: output file name
    :param lines: list
    :return: none
    '''
    f = open(filename, "w")
    for line in lines:
        if line == '' or line == '\n':
            continue
        else:
            f.write(line)
    f.close()
    return




if __name__ == '__main__':

    # Run for terminal

    input_file_name=sys.argv[-1]
    # handle input file name to get the output file name
    prefix_index=input_file_name.find(".in")
    # get the prefix
    prefix=input_file_name[0:prefix_index]
    # get the output file name
    output_file_name=prefix+".out"

    lines=remove_comment_from_file(input_file_name)
    write_result(output_file_name,lines)
    exit(0)

    # if you want to test in IDE uncomment the below and comment the above in main function
    '''
    input_file_name=input()
    # handle input file name to get the output file name
    prefix_index=input_file_name.find(".in")
    prefix=input_file_name[0:prefix_index]
    output_file_name=prefix+".out"

    lines=remove_comment_from_file(input_file_name)
    output_result(lines)
    write_result(output_file_name,lines)
    exit(0)
    '''


