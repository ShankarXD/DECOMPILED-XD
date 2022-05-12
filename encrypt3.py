import marshal, os, time


def main():
    try:
    	os.system('clear')
        a = input('(+) masukan file : ')
        x = open(a).read()
        b = compile(x, '<code>', 'exec')
        c = a.replace('.py', '_enc.py')
        d = marshal.dumps(b)
        e = open(c, 'w')
        e.write('# Compiled by SHANKAR-XD\n# Github  : https://github.com/SHANKAR-XD\n')
        e.write('import marshal\n')
        e.write('exec(marshal.loads(' + repr(d) + '))')
        e.close()
        time.sleep(2)
        print('\n(+) Selesai...')
    except IOError:
        print('\n(+) File Tidak Ditemukan !!!')
        exit()
    except KeyboardInterrupt:
        exit()


main()
