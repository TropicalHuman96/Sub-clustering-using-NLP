import logging
import os
from sklearn.cluster import KMeans
import gensim

# Reads and returns the list of files from a directory
def read_directory(mypath):
    current_list_of_files = []

    while True:
        for (_, _, filenames) in os.walk(mypath):
            current_list_of_files = filenames
        logging.info("Reading the directory for the list of file names")
        return current_list_of_files


# Function you will be working with
def creating_subclusters(list_of_terms, name_of_file):
    # Your code that converts the cluster into subclusters and saves the output in the output folder with the same name as input file
    # Note the writing to file has to be handled by you.
     model = gensim.models.Word2Vec(iter=1) 
     mtx=[[0 for i in range(100)] for i in range(100)]
     for i in range(len(list_of_terms)):
        for j in range(len(list_of_terms)):
            mtx[i][j]=model.similarity(list_of_terms[i],list_of_terms[j])
     print(list_of_terms)
     kmeans = KMeans(n_clusters=2)
     # Fitting the input data
     kmeans = kmeans.fit(mtx)
     labels = kmeans.predict(mtx)
     # in row_dict we store actual meanings of rows
     row_dict=[]
     for i in range(100):
         row_dict[i]=i+1
     clusters = {}
     n = 0
     p=[]
     q=[]
     for item in labels:
         if item in clusters:
             clusters[item].append(row_dict[n])
         else:
             clusters[item] = [row_dict[n]]
             n +=1
     for item in clusters:
         for i in clusters[item]:
            if clusters[item]==1:
                p=p.append(list_of_terms[i])
            else:
                q=q.append(list_of_terms[i])
     
     with open("%s.txt"%name_of_file,"w") as name_of_file:
         name_of_file.write(p,"\n",q)
     

# Main function
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

    # Folder where the input files are present
    mypath = "input"
    list_of_input_files = read_directory(mypath)
    for each_file in list_of_input_files:
        with open(os.path.join(mypath, each_file), "r") as f:
            file_contents = f.read()
        list_of_term_in_cluster = file_contents.split()

        # Sending the terms to be converted to subclusters in your code
        creating_subclusters(list_of_term_in_cluster, each_file)

        # End of code