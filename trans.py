import os
from xml.dom.minidom import parse
import cv2

a = os.listdir('bitfsd_dataset/annotations')
print(len(a))

img = cv2.imread('bitfsd_dataset/JPEGImage/0.jpg')
# img.show()
img = cv2.vconcat([img, img])
cv2.imwrite('haha.jpg', img)
tot = 0
for i in a:
    print(str(i), str(tot/(len(a))))
    tot += 1
    file = i
    img = cv2.imread('bitfsd_dataset/JPEGImage/' + str(file[:-4]) + '.jpg')
    img = cv2.vconcat([img, img])
    cv2.imwrite('dataset/jpeg/' + str(file[:-4]) + '.jpg', img)
    domTree = parse('bitfsd_dataset/annotations/' + str(file))
    rootNode = domTree.documentElement
    height = rootNode.getElementsByTagName('height')[0]
    height.childNodes[0].data = 1180
    object_sub = rootNode.getElementsByTagName('object')
    # print(len(object_sub))
    

    # custiomer_node = domTree.createElement("customer")
    for j in object_sub:
        # print(j)
        # name = j.getElementsByTagName("name")[0].childNodes[0].data
        # print(name)
        name_old = j.getElementsByTagName("name")[0].childNodes[0].data
        xmin_old = j.getElementsByTagName("xmin")[0].childNodes[0].data
        xmax_old = j.getElementsByTagName("xmax")[0].childNodes[0].data
        ymin_old = j.getElementsByTagName("ymin")[0].childNodes[0].data
        ymax_old = j.getElementsByTagName("ymax")[0].childNodes[0].data

        new_obj= domTree.createElement("object")

        name_new = domTree.createElement("name")
        name_new_data = domTree.createTextNode(name_old)
        name_new.appendChild(name_new_data)
        new_obj.appendChild(name_new)

        pose_new = domTree.createElement("pose")
        pose_new_Data = domTree.createTextNode("Unspecified")
        pose_new.appendChild(pose_new_Data)
        new_obj.appendChild(pose_new)

        truncated_new = domTree.createElement("truncated")
        truncated_new_data = domTree.createTextNode("0")
        truncated_new.appendChild(truncated_new_data)
        new_obj.appendChild(truncated_new)

        difficult_new = domTree.createElement("difficult")
        difficult_new_data = domTree.createTextNode("0")
        difficult_new.appendChild(difficult_new_data)
        new_obj.appendChild(difficult_new)

        occluded_new = domTree.createElement("occluded")
        occluded_new_data = domTree.createTextNode("0")
        occluded_new.appendChild(occluded_new_data)
        new_obj.appendChild(occluded_new)

        bndbox_new = domTree.createElement("bndbox")
        xmin_new = domTree.createElement("xmin")
        xmin_new_data = domTree.createTextNode(xmin_old)
        xmin_new.appendChild(xmin_new_data)
        xmax_new = domTree.createElement("xmax")
        xmax_new_data = domTree.createTextNode(xmax_old)
        xmax_new.appendChild(xmax_new_data)
        ymin_new = domTree.createElement("ymin")
        ymin_new_data = domTree.createTextNode(str(int(ymin_old)+590))
        ymin_new.appendChild(ymin_new_data)
        ymax_new = domTree.createElement("ymax")
        ymax_new_data = domTree.createTextNode(str(int(ymax_old)+590))
        ymax_new.appendChild(ymax_new_data)
        bndbox_new.appendChild(xmin_new)
        bndbox_new.appendChild(xmax_new)
        bndbox_new.appendChild(ymin_new)
        bndbox_new.appendChild(ymax_new)
        new_obj.appendChild(bndbox_new)



        # new_obj = j
        rootNode.appendChild(new_obj)



    with open('dataset/annotation/' + str(file), 'w') as f:
        domTree.writexml(f, addindent=' ', encoding='utf-8')
    # break
