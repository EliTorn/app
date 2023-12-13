import streamlit as st


def add():
    st.subheader("חיבור ")
    csharp_code = """
           
namespace HelloWorld
{
    class Program
    {
        public static void Main(string[] args)
        {
            int num1 = 3;
            int num2 = 4;
            int sum = num1 + num2;
            Console.WriteLine(sum);
        }
    }
}




                           """
    st.code(csharp_code, language='csharp')


def subtraction():
    st.subheader("חיסור ")
    csharp_code = """

    namespace HelloWorld
    {
        class Program
        {
            public static void Main(string[] args)
            {
                int num1 = 3;
                int num2 = 4;
                int sum = num1 - num2;
                Console.WriteLine(sum);
            }
        }
    }




                               """
    st.code(csharp_code, language='csharp')


def mult():
    st.subheader("כפל ")
    csharp_code = """

    namespace HelloWorld
    {
        class Program
        {
            public static void Main(string[] args)
            {
                int num1 = 3;
                int num2 = 4;
                int sum = num1 * num2;
                Console.WriteLine(sum);
            }
        }
    }




                               """
    st.code(csharp_code, language='csharp')


def division():
    st.subheader("חילוק ")
    csharp_code = """

    namespace HelloWorld
    {
        class Program
        {
            public static void Main(string[] args)
            {
                int num1 = 3;
                int num2 = 4;
                int sum = num1 / num2;
                Console.WriteLine(sum);
            }
        }
    }




                               """
    st.code(csharp_code, language='csharp')


def modol1():
    st.subheader("דוגמא ראשונה ")
    csharp_code = """

        
namespace HelloWorld
{
    class Program
    {
        public static void Main(string[] args)
        {
            int num = 5 % 2;
            Console.WriteLine(num);
        }
    }
}






                                   """
    st.code(csharp_code, language='csharp')
