# Submitter: bmorton(Morton, Brad)
import prompt 
from goody       import safe_open,irange
from collections import defaultdict # Use defaultdict for prefix and query


def all_prefixes(fq : (str,)) -> {(str,)}:
    return {fq[:num+1] for num in range(len(fq))}



def add_query(prefix : {(str,):{(str,)}}, query : {(str,):int}, new_query : (str,)) -> None:
    query[new_query]+=1
    for item in list(all_prefixes(new_query)):
        prefix[item].add(new_query) 
    

def read_queries(open_file : open) -> ({(str,):{(str,)}}, {(str,):int}):
    p,q=defaultdict(set),defaultdict(int)
    for line in open_file:
        nq=tuple(line.strip('\n').split(' '))
        add_query(p,q,nq)
    return p,q


def dict_as_str(d : {None:None}, key : callable=None, reverse : bool=False) -> str:
    return ''.join(['  '+str(item)+' -> '+str(d[item])+'\n' for item in sorted(d.keys(),key=key,reverse=reverse)])


def top_n(a_prefix : (str,), n : int, prefix : {(str,):{(str,)}}, query : {(str,):int}) -> [(str,)]:
    try:
        i=sorted([item for item in query.values()], reverse=True)
        result=[]
        for item1 in i:
            for item2 in reversed(list(query.keys())):
                if item2 in prefix[a_prefix] and query[item2]==item1 and item2 not in result:
                    result.append(item2)
    except:
        return []
    return result[0:n]
                
        




# Script

if __name__ == '__main__':

    file=input('Enter the name of any file with the full queries: ')
    d1=read_queries(open(file))
    print()
    print('Prefix dictionary:')
    print(dict_as_str(d1[0]))
    print()
    print('Query dictionary:')
    print(dict_as_str(d1[1]))
    while True:
        p=tuple(input('Enter any prefix (or quit): ').split())
        if p[0]=='quit':
            break
        print('Top 3 (or fewer) full queries = ',top_n(p, 3, d1[0], d1[1]))
        print()
        q=tuple(input('Enter any full query (or quit): ').split())
        if q[0]=='quit':
            break
        add_query(d1[0], d1[1], q)
        print()
        print('Prefix dictionary:')
        print(dict_as_str(d1[0]))
        print()
        print('Query dictionary:')
        print(dict_as_str(d1[1]))

    print()
#    import driver
#    driver.default_file_name = "bsc5.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
#    driver.driver()
