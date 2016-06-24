import os
import sys

def readRoc(path):
    cnt = 0
    result = []
    for line in open(path):
        result.append(line.split(':')[1].strip());
    return result

def writeResult(fid, result):
    for acc in result:
        fid.write(acc + '\t')
    fid.write('\n')

def main(argv):
    cmd_str     = argv[0]
    result_path = argv[1]
    start       = int(argv[2])
    internal    = int(argv[3])
    end         = int(argv[4])

    save_path = result_path + '/' + cmd_str.replace('--', '') + '_' + str(start) + '_to_' + str(end) + '_results.txt'
    fid = open(save_path, 'w')
    print cmd_str
    result = []

    for i in range(start, end+1, internal):
        if cmp(cmd_str, '--CD3000') == 0:
            path = result_path + '/' + 'CD3000_man5pt_' + str(i) + '0k/CD3000_man5pt_' + str(i) +'0k_roc.txt'         
            result = (readRoc(path))
            writeResult(fid, result)

        elif cmp(cmd_str, '--LFW') == 0:
            path = result_path + '/' + 'lfw_man5pt_' + str(i) + '0k/lfw_man5pt_' + str(i) +'0k_roc.txt'
            result = (readRoc(path))
            writeResult(fid, result)
            
        elif cmp(cmd_str, '--HSIdent') == 0:
            path = result_path + '/' + 'HSIdent_5pt_' + str(i) + '0k/HSIdent_5pt_' + str(i) +'0k_roc.txt'
            result = (readRoc(path))
            writeResult(fid, result)
            
        else:
            print 'Unknown command'

    fid.close()



if __name__ == '__main__':
    main(sys.argv[1:])