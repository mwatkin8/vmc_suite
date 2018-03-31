all:
	go get "github.com/brentp/vcfgo"
	go get "github.com/brentp/xopen"
	go get "github.com/mwatkin8/copy_go-vmc/vmc"
	go build -buildmode=c-shared -o govcf-vmc.so govcf-vmc.go
	#code to install vmccl
	#wget https://github.com/srynobio/vmccl/releases/download/v1.0.0/vmccl_linux64 /usr/local/bin
 	#mv /usr/local/bin/vmccl_linux64 /usr/local/bin/vmccl
 	#chmod a+x /usr/local/binvmccl
