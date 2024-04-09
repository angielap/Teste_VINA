import os
entrada = ["20-Hydroxyecdysone","Ecdysone","Methoxyfenozide","Ponasterone-A","Tebufenozide","Glucose","Hexane","Benzene","Phenol",
"Ligand1","Ligand2","Ligand3","Ligand4","Ligand5","Ligand6","Ligand7","Ligand8","Ligand9","Ligand10","Ligand11","Ligand12","Ligand13","Ligand14","Ligand15",
"Ligand16","Ligand17","Ligand18","Ligand19a","Ligand19b","Ligand19d","Ligand19g","Ligand20","Ligand21","Ligand22","Ligand23a","Ligand24","Ligand25","Ligand26",
"Ligand27","Ligand28","Ligand29","Ligand30","ZINC967513","ZINC1531550","ZINC8234282","ZINC30730221","ZINC100086523","ZINC2019619","ZINC968230","ZINC85644544",
"ZINC86034080","ZINC968225","ZINC59778864","ZINC62237753","ZINC968468","ZINC70454368","ZINC100780735","ZINC59778570","ZINC64624831","ZINC1648304","ZINC15121415",
"ZINC409176","ZINC490","ZINC175245225","ZINC2169363","ZINC1530331","ZINC57988166","ZINC59200506","ZINC38139375","ZINC13380906","ZINC57989172","ZINC8220462",
"ZINC4081998","ZINC5767672","ZINC141973482","ZINC85599405","ZINC1851022","ZINC967583","ZINC3861087","ZINC1686990","ZINC100782219","ZINC388674","ZINC13429400",
"ZINC968099","ZINC59587780","ZINC15120743","ZINC1531610","ZINC967594","ZINC1411","ZINC70451264","ZINC85880213","ZINC64634151","ZINC32142970","ZINC100199761",
"ZINC90734947","ZINC201364957","ZINC1531601","ZINC1529208","ZINC100028042","ZINC100155602","ZINC142456176","ZINC1531621","ZINC1531619","ZINC1529819","ZINC56874358",
"ZINC59206468","ZINC1846611","ZINC83260318","ZINC58257","ZINC8234296","ZINC85664165","ZINC100232131","ZINC70454426","ZINC32166631","ZINC896628","ZINC2600024",
"ZINC137919391","ZINC111473060","ZINC195760538","ZINC165056935","ZINC348140","ZINC32176608","ZINC33841709","ZINC2010172","ZINC96334604","ZINC85867164","ZINC5158152",
"ZINC85644689","ZINC230878335","ZINC32217531","ZINC143807786","ZINC1850881","ZINC1531600","ZINC4102279","ZINC136696735","ZINC968030","ZINC59200507","ZINC59778978",
"ZINC2035755","ZINC59587245","ZINC1699438","ZINC1699439","ZINC968246","ZINC968250","ZINC967593","ZINC967520","ZINC967800","ZINC14588455","ZINC4098372","ZINC12153091",
"ZINC2508248","ZINC968287","ZINC967511","ZINC2559334","ZINC968028","ZINC967597","ZINC4262096","ZINC967599","ZINC967601","ZINC4410593","ZINC967816","ZINC100075761",
"ZINC59586886","ZINC30731544","ZINC238399989","ZINC968471","ZINC2018831","ZINC2083320","ZINC4098262","ZINC1996067","ZINC6071066","ZINC12358735","ZINC12358780",
"ZINC967635","ZINC1676040","ZINC5158074","ZINC1529247","ZINC2512204","ZINC1653216"]
for e in entrada:
	os.system("vina_split --input out"+e+"receptor1.rigid.pdbqt --flex "+e+"EcdRecAgonist --ligand "+e+"a")