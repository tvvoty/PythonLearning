from pysubparser import parser
import freqlist
import MeCab


#put there absolute path of the file with double slashes eg 'E:\PythonProjects\pythonProject1\Anime frec list\[Kamigami] Barakamon - 01 [1280×720 x264 AAC Sub(Chs,Jap)].ass'
sub_file = 'put there path of the file'
subtitles = parser.parse('E:\\PythonProjects\\pythonProject1\\Anime frec list\\[Kamigami] Barakamon - 01 [1280×720 x264 AAC Sub(Chs,Jap)].ass')

wakati = MeCab.Tagger("-Owakati")

for subtitle in subtitles:
    subline = subtitle
    #print(subtitle.text)
    line_splitted = (wakati.parse(subtitle.text).split())
    freqlist.
    print(line_splitted)
