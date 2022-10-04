% RV and QoI are matrices with size of (nsamp x ndim) 
% nsamp: number of samples
% ndim : number of RVs or QoIs

fileID = fopen('RV.bin','w');
fwrite(fileID,RV','float'); % RV matrix is transposed because Matlab uses column-major binary
fclose(fileID);

fileID = fopen('QoI.bin','w');
fwrite(fileID,QoI','float'); % QoI matrix is transposed because Matlab uses column-major binary
fclose(fileID);

