def process_file(reader: textIO) -> None:
    """ Reader and print the data from reader, which must start with a single description line,
    then a sequence of lines beginning with '#', then a sequence of data.
    
    >>> infile = StringI0('Example\\n# Comment\\nLine 2\\n')
    >>> process_file(infile)
    Line 1
    Line 2
    """
    
    #Find and print the first piece of data
    line = skip_header(reader).strip()
    print(line)
    
    #Read the rest of the data
    for line in reader:
      line = line.strip()
      print(line)
      
if __name__ =='__main__':
  wite open('hopedale.txt, 'r') as input_file:
            process_file(input_file)
    
