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
        data[i] = n;  
    }

    public void pushback(int n) {
        // [1, 2, 3, 4], size = 4, capacity = 4
        // pushback(2); --> [1, 3, 4, 2] 2 at size
        // 
        if (size == capacity) {
            resize();
        }
        data[size] = n;
        size++;
    }

    public int popback() {
        int removed = data[size - 1];
        data[size - 1] = 0;
        size--;
        return removed;
    }

    private void resize() {
        capacity = capacity * 2;
        int[] new_data = new int[capacity];

        for (int i = 0; i < data.length; i++) {
            new_data[i] = data[i];
        }
        data = new_data;
    }

    public int getSize() {
        return size;
    }

    public int getCapacity() {
        return capacity;
    }
}

