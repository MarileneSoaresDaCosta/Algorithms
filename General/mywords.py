
t = raw_input().strip()
t = int(t)
outputwords = []
word_i = 0
for word_i in xrange(t):
   word = str(raw_input().strip())
   outputwords.append(word)

print 'end of output words'
print

t = raw_input().strip()
t = int(t)
mywords = []
word_i = 0
for word_i in xrange(t):
   word = str(raw_input().strip())
   mywords.append(word)

print 'end of mywords'
print
print 'comparing two lists'

zipped = zip(outputwords, mywords)
for i in range(0, len(zipped)):
  if zipped[i][0] != zipped[i][1]:
      print 'out:', zipped[i][0], 'my:', zipped[i][1]

print 'end'



# their output
"""
imllmmcslslkyoegyoam
fvincndjrurhf
rtglgzzqxnuflitnlyti
mhtvaqofxtyzr
zalqxykemvzzgkaa
wjjulziszbqqdcpdnhod
japjbvjlxzkgietmk
jqczvgqywydkunmwj
ehdegnmorgafrjxvsck
tydwixlwghlomq
wddnwjneaxbwhwarm
pnimbesirfbixlv
mijamkzpiiniveki
qxtwpdpwexuje
qtcshorwykc
xoojiggdcyjrurp
vcjmvngcdyabcmzj
xildrrpach
rrcntnbqchsfhvjhi
kmotatmrabtcoum
bnfcejmyotwv
dnppdkpywiaxddoxq
tmowsxkrodmkrak
jfkaehlegowfggh
ttylsiegnttymxty
kyetllczuyibdkwyiqhr
xdhqbvlbtmmtshejff
kpdpzzohihzwgdgbfz
kuywptftpaaa
qfqpegznnyludvr
ufwogufbzaboaepsliqk
jfejqapjvbdcxtkyr
sypjbvatgiodddxy
wdpfyqjcpnc
baabpjckkyturd
uvwurzjyzbhcqmryprqa
kvtwtmqygksbmi
ivsjycnooeodwtp
zqyxjnnitzawipsmq
blmrzavodtfzyezp
bmqlhqndavc
phvauobwkrcfwdedcs
vpygyqubqywkndhwpz
yikanhdrwjx
vnpblfxmvwkflqokbr
pserilwzxwyorldsxlks
qymbqaehnyzhfqpqrlpp
fcakwzuqlzglnidbkmq
jkscckttaeifiksgkxmx
dkbllravwnhhfjjrec
imzsyrykfvtj
tvogoocldlukwfcajvxi
cvnagtypozljprajglv
hwcmacxvsmu
rhrzcpprqcfc
clppxvwtaktchqrfdi
qwusnlldnolqh
yitverajov
arciyxaxtvmfgqwbu
pzbxvxdjuuvvu
nxfowilpdxwltp
swzsaynxbytyttqq
qyrogefletey
iotjgthvslvmjpcchufh
knfpyjtzqf
tmtbfayantwkm
asxwzygnngw
rmwiwrurutb
bhmpfwhgqfcqfldlsh
yhbidtewppg
jwwbeuiklpodziiv
anjhprmkwieb
lpwhqaebrm
dunecynelymcpyonqj
hblfldireuivzekegti
uryygzpwifrriecgvw
kzuhaysegaxtwqtxv
kvarmrbpoxxujhvgwp
hanhaggqzdpunkugzmqh
gnwqwsylqeurq
qzkjbnyvclrkmtcd
argsnaqbqvu
obbnlkoaklxc
ojiilqieycsasvqosyuc
qhlgiwsmtxbffjtsx
vvrvnmndeopgy
ibeqzyeuvzbf
sajpyegttujyxx
zmdjphzogfldlkgbchtn
tbanvjmwixrx
gmdhdlmopzyvddeyajjq
yxvmvedubzdcp
soygdzhbckkfu
gkbekyrhwcc
wevzqpnqwtpuf
rbobquotbysufwqjoe
bpgqfwoyntuhkwov
schtabphairewhfpm
rlmrahlisggguykue
fjtfrmlqvseqk
"""





# my words
""" 
fvincndjrurhf
imllmmcslslkyoegyoam
rtglgzzqxnuflitnlyti
mhtvaqofxtyzr
zalqxykemvzzgkaa
wjjulziszbqqdcpdnhod
japjbvjlxzkgietmk
jqczvgqywydkunmwj
ehdegnmorgcafjkrsvx
tydwixlwghlomq
wddnwjneaxbwhwarm
pnimbesirfblivx
mijamkzpiiniveki
qxtwpdpwexuje
qtcshorwykc
xoojiggdcyjrurp
vcjmvngcdyabcmzj
xildrrpach
rrcntnbqchshfhijv
kmotatmrabtcoum
bnfcejmyotwv
dnppdkpywiaxddoxq
tmowsxkrodmkrak
jfkaehlfeggghow
ttylsiegnttymxty
kyetllczuyibdkwyiqhr
xdhqbvlbtmmtshfefj
kpdpzzohihzwgdgbfz
kuywptftpaaa
qfqpegznnyludvr
ufwogufbzaboaepsliqk
jfejqapjvbdcxtkyr
sypjbvdaddgiotxy
wdpfyqjcpnc
baabpjckkyturd
uvwurzjyzbhcqmryprqa
kvtwtmqygksbmi
ivsjycnooeodwtp
zqyxjnnitzawmipqs
blmrzavodtfzyezp
bmqlhqndavc
phvauobwkrcfwdedcs
vpygyqubqywkndhwpz
yikanhdrwjx
vnpblfxmvwkflqokbr
pserilwzxwyorldsxlks
qymbqaehnyzhlfpppqqr
fcakwzuqlzglnidbkmq
jkscckttaeifiksgkxmx
dkbllravwnhhfjjrec
imzsyrykfvtj
tvogoocldlukwfcajvxi
cvnagtypozljprajglv
hwcmacxvsmu
rhrzcpprqcfc
clppxvwtaktchqrfdi
qwusnlldnolqh
yitvjaeorv
arciyxbafgmqtuvwx
pzbxvxdjuuvvu
nxfowilpdxwltp
swzsaynxqbqtttyy
qyrogefletey
iotjgthvslvmjpcfchhu
knfpyjtzqf
tmtbfaykamntw
asxwzygnngw
rmwiwrurutb
bhmpfwhgqfcqfldlsh
yhbidtewppg
jwwbeuiklpoidivz
anjhprmkwieb
lpwhqaebrm
dunecynelymcpyonqj
hblfldireuivzekegti
uryygzpwifrriecgvw
kzuhaysegaxtwqtxv
kvarmrbpoxxujhvgwp
hanhaggqzdpunkugzmqh
gnwqwsylqeurq
qzkjcbcdklmnrtvy
argsnaqbqvu
obbnlkoaklxc
ojiilqieycsasvqosyuc
qhlgiwsmtxbffjtsx
vvrvnmndeopgy
ibeqzyeuvzbf
sajpyegttuxjxy
zmdjphzogfldlkgbchtn
tbanvjmwixrx
gmdhdlmopzyvddjaejqy
yxvmvedubzdcp
soygdzhbckkfu
gkcbcehkrwy
wevzqpnqwtpuf
rbobquotbysufwqjoe
bpgqfwoyntuhokvw
schtabphairewhfpm
rlmrahlisggguykue
fjtfrmlqvseqk
"""