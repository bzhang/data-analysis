rm(list=ls())
# dataPath = "/Volumes/BigTwins/MutatorModelData/"
# outputPath = "/Volumes/BigTwins/Dropbox/MutatorModel/Results/"
dataPath = "~/Documents/MutatorModel"
outputPath = "~/Dropbox/MutatorModel/Results/"

setwd(dataPath)
# First column starts with 'd' which is a directory
# Nineth column starts with 'M' which is a result directory
# dirs <- system("ls -l ./ | awk '{if ($1~/^d/ && $9~/M0.5_R0.0_G4000_N500_BeneMR1.0E-6_DeleMR1.0E-4_BeneE1.1_DeleE0.9_MutStr2_MutaMR0.0010_Prob2M0.5_MutaE10/ || $9~/M0.5_R1.0_G4000_N500_BeneMR1.0E-6_DeleMR1.0E-4_BeneE1.1_DeleE0.9_MutStr2_MutaMR0.0010_Prob2M0.5_MutaE10/) print $9}'", intern=TRUE)
dirs <- system("ls -l ./ | awk '{if ($1~/^d/ && $9~/^MutCount_M0.0_R[01].0_G5000_N500_BeneMR3.162278E-4_DeleMR0.03162278_BeneE1.01_DeleE0.99_MutStr2_MutaMR0.0_Prob2M0.5_MutaE2/) print $9}'", intern=TRUE)
fileTitle = "MutCount_M0.0_R[01].0_G5000_N500_BeneMR3.162278E-4_DeleMR0.03162278_BeneE1.01_DeleE0.99_MutStr2_MutaMR0.0_Prob2M0.5_MutaE2"
figTitle = "NonEvolMutation_Dele_1e-1.5_1_100_Asex_Sex_MutE2_FE001_5000"
figTitleAsex = "NonEvolMutation_Dele_1e-1.5_1_100_Asex_MutE2_FE001_5000"
nGeneration = 5000

nPop = 100
nVariable = 4 # 2 if mutator exists
nDir = 2
# mat = matrix(nrow=nPop*nDir,ncol=nVariable*nGeneration)
sink("screenout.txt")
dirCounter = 0
for (i in dirs){
	popCounter = 1
	for (j in dir(i,full.names=T,pattern="txt")){ # j: the path of each file(pop)
		data = read.table(j,header=T,sep="\t")
		attach(data)
		names(data)
		exp = data.frame(FitnessMean,MutatorStrengthMean,nDeleMutMean,nBeneMutMean) # mutator exists
#		exp = data.frame(FitnessMean) # only non-mutator exists
		for (n in 1:length(exp[,1])){ # n: current generation #
			for (m in 1:length(exp[1,])){ # m: current variable
				# Mat row: 50 pops; Mat col: generations, (FitnessMean, MutatorStrengthMean),(FitnessMean, MutatorStrengthMean)...
				# mat[(dirCounter*nPop+popCounter),(n-1)*length(exp[1,])+m] = exp[n,m]				
				if (i == 1){
					asexFitness[1,]					
				}
			}
		}
		popCounter = popCounter + 1
	}
	dirCounter = dirCounter + 1
}
sink()


ErrBar<-function(mat,n) {
	mmat=matrix(nrow=1,ncol=nVariable*nGeneration)
	lmat=matrix(nrow=1,ncol=nVariable*nGeneration)
	umat=matrix(nrow=1,ncol=nVariable*nGeneration)
	mAll=apply(mat,2,mean,na.rm=T)
	sAll=apply(mat,2,sd,na.rm=T)
	seAll=sAll/n
	lowerAll=mAll-seAll*qt(0.975,df=n-1)
	upperAll=mAll+seAll*qt(0.975,df=n-1)
	mmat[1,]=mAll
	lmat[1,]=lowerAll
	umat[1,]=upperAll
	return(list(mmat=mmat, lmat=lmat, umat=umat))
}

list.result=ErrBar(mat[1:nPop,],nPop)
asexMatM=list.result$mmat
asexMatL=list.result$lmat
asexMatU=list.result$umat

list.result=ErrBar(mat[(nPop+1):(nPop*nDir),],nPop)
sexMatM=list.result$mmat
sexMatL=list.result$lmat
sexMatU=list.result$umat

asexMatMF = matrix(nrow=1,ncol=nGeneration)
asexMatLF = matrix(nrow=1,ncol=nGeneration)
asexMatUF = matrix(nrow=1,ncol=nGeneration)
asexMatMM = matrix(nrow=1,ncol=nGeneration)
asexMatLM = matrix(nrow=1,ncol=nGeneration)
asexMatUM = matrix(nrow=1,ncol=nGeneration)
sexMatMF = matrix(nrow=1,ncol=nGeneration)
sexMatLF = matrix(nrow=1,ncol=nGeneration)
sexMatUF = matrix(nrow=1,ncol=nGeneration)
sexMatMM = matrix(nrow=1,ncol=nGeneration)
sexMatLM = matrix(nrow=1,ncol=nGeneration)
sexMatUM = matrix(nrow=1,ncol=nGeneration)

for (i in 1:nGeneration){ # Mat: one row: (Fitness,Mutator),...
	asexMatMF[i] = asexMatM[i*2-1] # Mat F: Fitness
	asexMatLF[i] = asexMatL[i*2-1]
	asexMatUF[i] = asexMatU[i*2-1]
	asexMatMM[i] = asexMatM[i*2] # Mat M: Mutator
	asexMatLM[i] = asexMatL[i*2]
	asexMatUM[i] = asexMatU[i*2]
	
	sexMatMF[i] = sexMatM[i*2-1] # Mat F: Fitness
	sexMatLF[i] = sexMatL[i*2-1]
	sexMatUF[i] = sexMatU[i*2-1]
	sexMatMM[i] = sexMatM[i*2] # Mat M: Mutator
	sexMatLM[i] = sexMatL[i*2]
	sexMatUM[i] = sexMatU[i*2]
}

plotx<-function(g,m,l,u,yl,rl,ru) {
	plot(g,m,type="n",cex=1.25,col="black",ylim=range(c(rl,ru)),xlab="Generations",ylab=yl) 
#xaxp=c(0,20000,20)
	for(j in 1:length(g)){
		segments(g[j],m[j],g[j],l[j],col="gray")
		segments(g[j],m[j],g[j],u[j],col="gray")
	}
	points(g,m,type="l",lwd=1,col="black")
}

plotWithoutErrorBar<-function(g,m,l,u,yl,rl,ru) {
	plot(g,m,type="n",cex=1.25,col="black",ylim=range(c(rl,ru)),xlab="Generations",ylab=yl) 
#xaxp=c(0,20000,20)
	# for(j in 1:length(g)){
	# 	segments(g[j],m[j],g[j],l[j],col="gray")
	# 	segments(g[j],m[j],g[j],u[j],col="gray")
	# }
	points(g,m,type="l",lwd=1,col="black")
}

plotPoints<-function(g,m,l,u) {
	for(j in 1:length(g)){
		segments(g[j],m[j],g[j],l[j],col="gray")
		segments(g[j],m[j],g[j],u[j],col="gray")
	}
	points(g,m,type="l",pch=21,col="red")
}

plotPointsWithoutErrorBar<-function(g,m,l,u) {
	# for(j in 1:length(g)){
	# 	segments(g[j],m[j],g[j],l[j],col="gray")
	# 	segments(g[j],m[j],g[j],u[j],col="gray")
	# }
	points(g,m,type="l",pch=21,col="red")
}


pdf(paste(outputPath, fileTitle,".pdf",sep=""),height=10,width=20)
par(mfrow=c(1,2),cex.axis=1.0, cex.lab=1.25, mar=c(5,5,2,2), bty="n")

plotx(c(1:nGeneration),asexMatMF,asexMatLF,asexMatUF,"Mean Fitness",min(asexMatLF,sexMatLF),max(asexMatUF,sexMatUF))
title(main=figTitle)
plotPoints(c(1:nGeneration),sexMatMF,sexMatLF,sexMatUF)

# plotWithoutErrorBar(c(1:nGeneration),asexMatMF,asexMatLF,asexMatUF,"Mean Fitness",min(asexMatLF,sexMatLF),max(asexMatUF,sexMatUF),min(asexMatLF,sexMatLF),max(asexMatUF,sexMatUF),20)
# title(main=figTitle)
# plotPointsWithoutErrorBar(c(1:nGeneration),sexMatMF,sexMatLF,sexMatUF)

plotx(c(1:nGeneration),asexMatMM,asexMatLM,asexMatUM,"Mean Mutator Strength",min(asexMatLM,sexMatLM),max(asexMatUM,sexMatUM))
title(main=figTitle)
plotPoints(c(1:nGeneration),sexMatMM,sexMatLM,sexMatUM)

# plotWithoutErrorBar(c(1:nGeneration),asexMatMM,asexMatLM,asexMatUM,"Mean Mutator Strength",min(asexMatLM,sexMatLM),max(asexMatUM,sexMatUM),min(asexMatLM,sexMatLM),max(asexMatUM,sexMatUM),20)
# title(main=figTitle)
# plotPointsWithoutErrorBar(c(1:nGeneration),sexMatMM,sexMatLM,sexMatUM)
dev.off()


# pdf(paste(outputPath, fileTitle,"_Asex.pdf",sep=""),height=10,width=20)
# par(mfrow=c(1,2),cex.axis=1.0, cex.lab=1.25, mar=c(5,5,2,2), bty="n")
# plotx(c(1:nGeneration),asexMatMF,asexMatLF,asexMatUF,"Mean Fitness",min(asexMatLF),max(asexMatUF))
# title(main=figTitleAsex)
# plotx(c(1:nGeneration),asexMatMM,asexMatLM,asexMatUM,"Mean Mutator Strength",min(asexMatLM),max(asexMatUM))
# title(main=figTitleAsex)
# dev.off()