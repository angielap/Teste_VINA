import os
# camando ligantes, receptor
ligantes = ["duloxetine", "chlorpromazine", "zotepine", "risperidone", "ergotamine", "apriprazole", "lisuride", "pscilocin", "lorcaserin", "methoxytryptamine", "cabergoline", "hydroxytryptamine", "lumateperone", "agomelatine", "haloperidol", "pindolol", "clozapine", "methysergide", "quizapine"]
receptor = ["SEagonist7wc7","SEantagonist6a94"]
config = "config.txt"
# preparando os receptores e convertendo de pdb para pdbqt (Loops)
for r in receptor:
	os.system("/home/angie/MGLTools-1.5.7/bin/pythonsh prepare_receptor4.py -r "+r+".pdb") #converte o arquivo do receptor para formato pdbqt
	for l in ligantes:
		os.system("/home/angie/MGLTools-1.5.7/bin/pythonsh prepare_ligand4.py -l "+l+".mol2") #converte o arquivo do ligante para formato pdbqt
		os.system("/home/angie/MGLTools-1.5.7/bin/vina --receptor "+r+".pdbqt --ligand "+l+".pdbqt --out ./output/"+l+r+".pdbqt --log ./log/"+l+r+".log --config config.txt") #comando que chama e executa o autodock vina
	
