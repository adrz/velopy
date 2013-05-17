clear all

[csv] = read_mixed_csv('13011.csv',',');


data = cellfun(@(s) {str2double(s)},csv(:,10));
data = cell2mat(data);
data = sort(data);
data = data - min(data);
%plot(data)
plot(diff(data)/1000)