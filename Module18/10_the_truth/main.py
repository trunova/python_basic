alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
specialSymbols = '"!,(\'/.'
text = 'vujgvmCfb tj ufscfu ouib z/vhm ' \
       'jdjuFyqm jt fscfuu uibo jdju/jnqm ' \
       'fTjnqm tj scfuuf ibou fy/dpnqm ' \
       'yDpnqmf jt cfuufs boui dbufe/dpnqmj ' \
       'uGmb tj fuufsc ouib oftufe/ ' \
       'bstfTq jt uufscf uibo otf/ef ' \
       'uzSfbebcjmj vout/dp ' \
       'djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ' \
       'ipvhiBmu zqsbdujdbmju fbutc uz/qvsj ' \
       'Fsspst tipvme wfsof qbtt foumz/tjm ' \
       'omfttV mjdjumzfyq odfe/tjmf ' \
       'Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv ' \
       'Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ ' \
       'Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud ' \
       'xOp tj scfuuf ibou /ofwfs ' \
       'uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op ' \
       'gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb ' \
       'Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ ' \
       'bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip '
answer = ''
s = ''
shift = 3
for i in range(len(text)):
    if text[i] in alphabet:
        s += alphabet[alphabet.index(text[i])-1]
    elif text[i] == ' ':
        if len(s) != 0:
            answer += s[len(s) - shift % len(s) :] + s[:len(s) - shift % len(s)]
        if '.' in s:
            answer += '\n'
            shift += 1
        else: answer += ' '
        s = ''
    elif text[i] in specialSymbols and text[i] != '.':
        s += specialSymbols[specialSymbols.index(text[i])+1]

print(answer)