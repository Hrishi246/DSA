def main():
    """
    General Info
    ------------
    For this challenge, you will be implementing a simple error counter.

    Your task is to build a program that takes a logfile to read, and prints
    the number of **404** errors from that file.

    Usage
    -----
    ::

      count_404s LOGFILE

    LOGFILE
      The path to the logfile to be inspected

    Result
    ------
    Prints the number of **404** errors from the file to stdout

    Notes
    -----

    You can use the example log file provided in /var/log/myservice/access_log to examine the
    file format and for initial testing development of your program::

      $ ~/bin/count_404s /var/log/myservice/access_log
      9
    You can run the `grader check count_404s` utility to test your program:

    #. either in normal mode with::

          $ grader check count_404s

    #. or in verbose / debug mode with::

          $ grader check count_404s -v

    Pro-tip: start by running the following on the command-line (without the leading '$')

      $ use python3 count_404s
    """
    count = 0
    l = open("/var/log/myservice/access_log", "r")
    for each in l.readlines():
        if "404" in each:
            count = count + 1
    return count


if __name__ == "__main__":
    main()