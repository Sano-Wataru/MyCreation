class Clothes {
    int id;
    String name;
    String category;
    double cindex;

    void print() {
        System.out.format("{id:%d, name:%s, category:%s, cindex:%.1f}\n", 
            id, name, category, cindex);
    }
}