def sep_fasta_file(name, name_w_r, name_w_l):
    b = False
    mark = '0'
    f_in = open(name, 'r')
    f_out_r = open(name_w_r, 'w')
    f_out_l = open(name_w_l, 'w')
    
    for line in f_in:
        
        if b and mark == 'r':
            mark = '0'
            b = False
            in_row = str(line.strip())
            f_out_r.write(in_row+'\n')
            
        if b and mark == 'l':
            mark = '0'
            b = False
            in_row = str(line.strip())
            f_out_l.write(in_row+'\n')
            
        if str(line.strip())[0] == '>' and str(line.strip())[-5:] == 'right':
            mark = 'r'
            b = True
            in_row = str(line.strip())
            f_out_r.write(in_row+'\n')
            
        if str(line.strip())[0] == '>' and str(line.strip())[-5:] == '_left':
            mark = 'l'
            b = True
            in_row = str(line.strip())
            f_out_l.write(in_row+'\n')
    f_in.close()
    f_out_r.close()
    f_out_l.close()
    
def main():

    name = 'C:/Users/Nek/Documents/bioinformaticsTasksPython/2in.txt'
    name_w_r = 'C:/Users/Nek/Documents/bioinformaticsTasksPython/2out_r.txt'
    name_w_l = 'C:/Users/Nek/Documents/bioinformaticsTasksPython/2out_l.txt'
    
    sep_fasta_file(name, name_w_r, name_w_l)

if __name__=='__main__':
    main()