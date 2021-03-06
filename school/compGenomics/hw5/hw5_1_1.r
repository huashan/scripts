##------------------------------
# a.	Write a program that receives input integers l,k,n, 
# chooses random n×n transition and n×k emission matrices 
# and produces an HMM output sequence 
# of length l of symbols 1,…,k .


myHW5_1 <- function(l, k, n) {
	# ##------------------------------parameter
	# l <- 10 # output sequence length
	# k <- 2	# observation
	# n <- 2  # state
	##------------------------------transition matrix
	# set.seed(100)
	tranMX <- matrix(runif(n^2),ncol=n)
	tranMX <- tranMX / rowSums(tranMX)
	colnames(tranMX) <- 1:n
	rownames(tranMX) <- 1:n 

	##------------------------------emission matrix
	# set.seed(100)
	emisMX <- matrix(runif(n*k),ncol=k)
	emisMX <- emisMX / rowSums(emisMX)
	colnames(emisMX) <- 1:k
	rownames(emisMX) <- 1:n

	##------------------------------start
	start <- runif(n)
	start <- start/sum(start)

	outMX  <- matrix(NA, nrow=l,ncol=n)

	outState  <- vector(length=l)
	outObserve <- vector(length=l)
	pointStateMX <- matrix(0,ncol=n,nrow=n)
	# outPSeq <- matrix(NA, ncol=n,nrow=l) 

	##------------------------------initiate
	temp <- log(start) + log(emisMX)
	outMX[1,] <- temp[,which.max(colSums(temp))]
	# rownames(outMX) <- 1:l
	# colnames(outMX) <- 1:n
	pointStateMX[1,] <- rep(0,n)
	outState[1] <- which.max(temp[,which.max(colSums(temp))])
	outObserve[1] <- which.max(colSums(temp))

	for(i in 2:l) {
		# print("previous out")
		# print(outMX[i-1,])
		temp1 <-  outMX[i-1,] + log(tranMX) 
		temp <- colSums(temp1) + log(emisMX)

		outMX[i,] <- temp[,which.max(colSums(temp))]
		# print("intermediea prob:")
		# print(temp)
		# outMX[i,] <- temp + log(apply(emisMX,1,max))
		outState[i] <- which.max(temp[,which.max(colSums(temp))])
		outObserve[i] <- which.max(colSums(temp))
	}
	# print(outObserve)
	return(outObserve)

}