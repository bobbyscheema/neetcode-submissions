class DynamicArray {
    int capacity;
    int size;
    int[] data;
    public DynamicArray(int capacity) {
        if (capacity < 0) {
            throw new IllegalArgumentException("Capacity is negative");
        }
        this.capacity = capacity;
        this.size = 0;
        this.data = new int[this.capacity];
    }

    public int get(int i) {
        return data[i];
       
    }

    public void set(int i, int n) {
        for (int index = 0; index < size; index++) {
            if (index == i) {
                data[i] = n;

            }
        }
    }

    public void pushback(int n) {
        // [1, 2, 3, 4], size = 4, capacity = 4
        // pushback(2); --> [1, 3, 4, 2] 2 at size
        // 
        if (size == capacity) {
            resize();
        }
        
        }
    }

    public int popback() {

    }

    private void resize() {

    }

    public int getSize() {

    }

    public int getCapacity() {

    }
}
