import MeCab
wakati = MeCab.Tagger("-Owakati")
#print(wakati.parse("pythonが大好きです").split())
# ['python', 'が', '大好き', 'です']


tagger = MeCab.Tagger()
print(tagger.parse("pythonが大好きです"))

#print(help(MeCab.Tagger))



# from fugashi import Tagger
#
# tagger = Tagger('-Owakati')
# text = "麩菓子は、麩を主材料とした日本の菓子。"
# tagger.parse(text)
# # => '麩 菓子 は 、 麩 を 主材 料 と し た 日本 の 菓子 。'
# for word in tagger(text):
#     print(word, word.feature.lemma, word.pos, sep='\t')
#     # "feature" is the Unidic feature data as a named tuple