import os
from shutil import rmtree, copy

def main():
  root = "."
  static_path = os.path.join(root, "static")
  public_path = os.path.join(root, "public")

  if os.path.exists(public_path):
    rmtree(public_path)

  os.mkdir(public_path)

  def copy_dir(path = ""):
    current_dir = os.path.join(static_path, path)
    new_dir = os.path.join(public_path, path)

    cd = os.listdir(current_dir)

    for item in cd:
      item_path = os.path.join(current_dir, item)
      copy_to = os.path.join(new_dir, item)

      if os.path.isfile(item_path):
        copy(item_path, new_dir)
      else:
        if not os.path.exists(copy_to):
          os.mkdir(copy_to)

        copy_dir(os.path.join(path, item))

  copy_dir()


if __name__ == "__main__":
  main()
