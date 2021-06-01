import cv2
from sklearn.cluster import KMeans

image=cv2.imread("sms1.jpg")
x,y,z= image.shape
#GET RGB FOR EACH PIXEL  &&  NEW SHAPE IS (X*Y,Z)

image_2d = image.reshape(-1,z)
#WANTED NUMBER OF CLUSTERS.

k_clusters= 7
kmeans_cluster = KMeans(n_clusters=k_clusters)
#FIT MODEL

kmeans_cluster.fit(image_2d)
cluster_centers = kmeans_cluster.cluster_centers_
#GET LABEL FOR EACH PIXEL

cluster_labels = kmeans_cluster.labels_
#IMAGE RECONSTRUCTION AND SAVE

cv2.imwrite("sms1_7_clusters.png",cluster_centers[cluster_labels].reshape(x,y,z))