"""Render the actual service-upload ZIPs, including their imported textures."""
from pathlib import Path
import argparse
import io
import zipfile
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
import trimesh


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", nargs="?", type=Path, default=Path(__file__).parent / "service-exports")
    parser.add_argument("--title", default="Neuronauts · revised service exports")
    args = parser.parse_args()
    directory = args.directory
    fig = plt.figure(figsize=(16, 5.5), facecolor="#f7f7f4")
    for i, (name, label) in enumerate([
            ("cortex", "Captain Cortex"), ("axon", "Axon"),
            ("dendra", "Dendra"), ("syn", "Syn"), ("glia", "Glia")]):
        with zipfile.ZipFile(directory / f"neuronaut-{name}-color-upload.zip") as z:
            obj = f"neuronaut-{name}.obj"
            mesh = trimesh.load(io.BytesIO(z.read(obj)), file_type="obj", force="mesh",
                                resolver=trimesh.resolvers.ZipResolver({n: z.read(n) for n in z.namelist()}),
                                process=False)
        colors = trimesh.visual.color.uv_to_color(
            mesh.visual.uv[mesh.faces].mean(axis=1), mesh.visual.material.image) / 255
        light = np.array([-0.3, 0.8, 0.6]); light /= np.linalg.norm(light)
        shade = 0.65 + 0.35 * np.maximum(mesh.face_normals @ light, 0)
        colors[:, :3] *= shade[:, None]
        ax = fig.add_subplot(1, 5, i + 1, projection="3d", facecolor="#f7f7f4")
        ax.add_collection3d(Poly3DCollection(mesh.triangles, facecolors=colors,
                                           edgecolors="none", linewidths=0))
        ax.set(xlim=(-28, 28), ylim=(-24, 24), zlim=(0, 75))
        ax.set_box_aspect((56, 48, 75))
        ax.view_init(elev=12, azim=78)
        ax.set_proj_type("ortho")
        ax.set_axis_off()
        ax.set_title(f"{label}\n{mesh.extents[2]:.1f} mm", fontsize=12, color="#18212b", pad=0)
    fig.suptitle(args.title, fontsize=21, color="#18212b", y=0.99)
    fig.text(0.5, 0.055, "Rendered from the upload files • full-color appearance preview; printed colors may vary",
             ha="center", fontsize=11, color="#5b6470")
    fig.subplots_adjust(left=0.01, right=0.99, top=0.86, bottom=0.08, wspace=-0.06)
    fig.savefig(directory / "crew-preview.png", dpi=150, facecolor=fig.get_facecolor())
    plt.close(fig)


if __name__ == "__main__":
    main()
