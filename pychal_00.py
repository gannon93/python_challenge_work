import os

try:
    from . import requests_helper as rh
except Exception:
    import requests_helper as rh

HERE = 'http://www.pythonchallenge.com/pc/def/0.html'
URL_BASE = os.path.split(HERE)[0]
URL_EXT = '.html'


def main():
    print('Solving Python Challenge {}:\n\t{}'.format(
        os.path.splitext(__file__)[0][-2:], HERE))
    answer = ''
    base_url = ''

    outfile = r'./pychal_a00.txt'
    with open(outfile, 'w') as out_fp:

        answer = str(2**38)
        base_url = os.path.join(URL_BASE, answer + URL_EXT)
        out_fp.write(base_url)

    print('Answer: ' + answer)
    rh.open(base_url)


if __name__ == '__main__':
    main()
