from pysubparser import parser

subtitles = parser.parse('Anime frec list//[Kamigami] Barakamon - 01 [1280×720 x264 AAC Sub(Chs,Jap)].ass')

# outputs springs
for subtitle in subtitles:
    print(subtitle.text)