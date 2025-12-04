import matplotlib.pyplot as plt
import cv2

img_path = "foto-solo.jpeg"
img = cv2.imread(img_path)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

points = []
gt_boxes = []

def onclick(event):
    global points, gt_boxes
    if event.xdata is not None and event.ydata is not None:
        points.append((int(event.xdata), int(event.ydata)))
        print(f"Click registrado: {points[-1]}")

        # Cada 2 clics = una caja
        if len(points) % 2 == 0:
            x1, y1 = points[-2]
            x2, y2 = points[-1]
            w, h = abs(x2 - x1), abs(y2 - y1)
            gt_box = [min(x1, x2), min(y1, y2), w, h]
            gt_boxes.append(gt_box)
            print("✅ Caja añadida:", gt_box)

            # Dibujar la caja
            ax.add_patch(plt.Rectangle((gt_box[0], gt_box[1]), w, h,
                                       fill=False, edgecolor='red', linewidth=2))
            fig.canvas.draw()

def onkeypress(event):
    global gt_boxes
    if event.key == 'q':  # pulsa 'q' para terminar
        print("\n👉 Selección finalizada")
        print("Todas las gt_boxes:", gt_boxes)
        fig.canvas.mpl_disconnect(cid_click)
        fig.canvas.mpl_disconnect(cid_key)

# Mostrar imagen y activar clicks
fig, ax = plt.subplots()
ax.imshow(img_rgb)

cid_click = fig.canvas.mpl_connect('button_press_event', onclick)
cid_key = fig.canvas.mpl_connect('key_press_event', onkeypress)
plt.show()
print("Pulsa 'q' para finalizar la selección de cajas.")