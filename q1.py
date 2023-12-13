import streamlit as st


def q1():

    csharp_code = """
    class A {
    public A() {
        System.out.println("class A");
    }
}

class B extends A{
    public B() {
        System.out.println("class B");
    }

    public static void main(String[] args) {
        A a = new A();
    }
}
      """
    st.code(csharp_code, language='java')
    st.markdown("""
       1. class B 
       2. runtime error 
       3. class A 
       class B
       4. compilation error
       5. class  B 
       class A 
       """)


def q2():

    csharp_code = """
class A {
    public A() {
        System.out.println("class A");
    }
}

class B extends A{
    public B() {
        System.out.println("class B");
    }

    public static void main(String[] args) {
        A a = new B();
    }
}
      """
    st.code(csharp_code, language='java')
    st.markdown("""
       1. class B 
           
       2. runtime error 
       3. class A 
       class B
       4. compilation error
       5. class  B 
       class A 
       """)


def q3():

    csharp_code = """
class A {
    public A() {
        System.out.println("class A");
    }
}

class B extends A{
    public B() {
        System.out.println("class B");
    }

    public static void main(String[] args) {
        B b = new A();
    }
}

      """
    st.code(csharp_code, language='java')
    st.markdown("""
       1. class B 

       2. runtime error 
       3. class A 
       class B
       4. compilation error
       5. class  B 
       class A 
       """)


def q4():
    csharp_code = """
class A {
    public A() {
        System.out.println("class A");
    }
}

class B {
    public B() {
        System.out.println("class B");
    }

    public static void main(String[] args) {
        B b = new B();
    }
}

      """
    st.code(csharp_code, language='java')
    st.markdown("""
       1. class B 

       2. runtime error 
       3. class A 
       class B
       4. compilation error
       5. class  B 
       class A 
       """)


def q5():

    csharp_code = """
class A {
    int x = 10;
}

class B extends A {
    int x = 5;
    public int getX() {
        return x;
    }

    public static void main(String[] args) {
        A a = new B();
        System.out.println(a.x);
    }
}

      """
    st.code(csharp_code, language='java')
    st.markdown("""
       1. 0
       2. runtime error 
       3. 10
       4. compilation error
       5. 5
       """)


def q6():

    csharp_code = """
class Counter {
    private static int count = 0;

    public Counter() {
        count++;
    }

    public static int getCount() {
        return count;
    }
}

public class Main {
    public static void main(String[] args) {
        Counter c1 = new Counter();
        Counter c2 = new Counter();
        Counter c3 = new Counter();

        System.out.println(Counter.getCount());
    }
}


      """
    st.code(csharp_code, language='java')
    st.markdown("""
       1. 0
       2. runtime error 
       3. 1
       4. compilation error
       5. 2
       6. 3 
       """)


def q7():

    csharp_code = """
    import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class ListManipulation {
    public static void main(String[] args) {
        List<String> arrayList = new ArrayList<>();
        List<String> linkedList = new LinkedList<>();

        arrayList.add("Element 1");
        arrayList.add("Element 2");
        arrayList.add("Element 3");

        linkedList.add("Element A");
        linkedList.add("Element B");
        linkedList.add("Element C");

        linkedList.addAll(arrayList.subList(1, 3));

        arrayList.set(2, "Modified Element");

        linkedList.remove("Element B");

        System.out.println("ArrayList: " + arrayList);
        System.out.println("LinkedList: " + linkedList);
    }
}

          """
    st.code(csharp_code, language='java')
    st.markdown("""
           1. The code will result in a compilation error.
2. The code will print the modified ArrayList and the modified LinkedList.
3. The code will print the original ArrayList and the modified LinkedList.
4. The code will print the modified ArrayList and the original LinkedList.
5. The code will print the original ArrayList and the original LinkedList.
6. The code will print an empty ArrayList and the modified LinkedList.
           """)


def q8():
    csharp_code = """
       import java.util.ArrayList;
import java.util.List;

public class ArrayListManipulationQuestion {
    public static void main(String[] args) {
        List<Integer> list1 = new ArrayList<>();
        List<Integer> list2 = new ArrayList<>();

        for (int i = 1; i <= 5; i++) {
            list1.add(i);
            list2.add(i * 10);
        }

        list2.addAll(list1.subList(1, 4));

        list1.set(3, 99);

        list2.remove(Integer.valueOf(20));

        System.out.println("List1: " + list1);
        System.out.println("List2: " + list2);
    }
}


              """
    st.code(csharp_code, language='java')
    st.markdown("""
            1.  The code will result in a compilation error.
2. The code will print the modified List1 and the modified List2.
3. The code will print the original List1 and the modified List2.
4. The code will print the modified List1 and the original List2.
5. The code will print the original List1 and the original List2.
6. The code will print an empty List1 and the modified List2.
               """)


def q9():
    csharp_code = """
    import java.util.HashMap;
import java.util.Map;

public class HashMapManipulationQuestion {
    public static void main(String[] args) {
        Map<String, Integer> map1 = new HashMap<>();
        Map<String, Integer> map2 = new HashMap<>();

        map1.put("A", 1);
        map1.put("B", 2);
        map1.put("C", 3);

        map2.put("X", 10);
        map2.put("Y", 20);
        map2.put("Z", 30);

        map2.putAll(map1);

        map1.put("B", 99);

        map2.remove("Y");

        System.out.println("Map1: " + map1);
        System.out.println("Map2: " + map2);
    }
}


              """
    st.code(csharp_code, language='java')
    st.markdown("""
1. The code will result in a compilation error.
2. The code will print the modified Map1 and the modified Map2.
3. The code will print the original Map1 and the modified Map2.
4. The code will print the modified Map1 and the original Map2.
5. The code will print the original Map1 and the original Map2.
6. The code will print an empty Map1 and the modified Map2.
               """)


def q10():
    csharp_code = """
    import java.util.HashSet;
import java.util.Set;

public class HashSetManipulationQuestion {
    public static void main(String[] args) {
        Set<Double> set1 = new HashSet<>();
        Set<Double> set2 = new HashSet<>();

        set1.add(1.5);
        set1.add(2.5);
        set1.add(3.5);

        set2.add(10.0);
        set2.add(20.0);
        set2.add(30.0);

        set2.addAll(set1);

        set1.remove(2.5);

        System.out.println("Set1: " + set1);
        System.out.println("Set2: " + set2);
    }
}

              """
    st.code(csharp_code, language='java')
    st.markdown("""
1. The code will result in a compilation error.
2. The code will print the modified Set1 and the modified Set2.
3. The code will print the original Set1 and the modified Set2.
4. The code will print the modified Set1 and the original Set2.
5. The code will print the original Set1 and the original Set2.
6. The code will print an empty Set1 and the modified Set2.
               """)


def q11():
    csharp_code = """
import java.util.HashSet;
import java.util.Set;

public class HashSetManipulationQuestion {
    public static void main(String[] args) {
        Set<String> set1 = new HashSet<>();
        Set<String> set2 = new HashSet<>();

        set1.add("Apple");
        set1.add("Banana");
        set1.add("Orange");

        set2.add("Banana");
        set2.add("Grapes");
        set2.add("Kiwi");

        set2.addAll(set1);

        set1.remove("Banana");

        System.out.println("Set1: " + set1);
        System.out.println("Set2: " + set2);
    }
}
              """
    st.code(csharp_code, language='java')
    st.markdown("""
1. The code will result in a compilation error.
2. The code will print the modified Set1 and the modified Set2.
3. The code will print the original Set1 and the modified Set2.
4. The code will print the modified Set1 and the original Set2.
5. The code will print the original Set1 and the original Set2.
6. The code will print an empty Set1 and the modified Set2.
               """)
