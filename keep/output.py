import streamlit as st


def writeLine():
    st.subheader("הדפסה רגילה ואחרי זה יורדים שורה")
    csharp_code = """
namespace HelloWorld
{
    class Program
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Hello world !");
            Console.WriteLine("My name is Eli");
            
        }
    }
}


               """
    st.code(csharp_code, language='csharp')


def write():
    st.subheader("הדפסה רגילה ולא יורדים שורה")
    csharp_code = """
    namespace HelloWorld
    {
        class Program
        {
            public static void Main(string[] args)
            {
                Console.Write("Hello ");
                Console.Write("World !");

            }
        }
    }


                   """
    st.code(csharp_code, language='csharp')


def number():
    st.subheader("הדפסת מספר")
    csharp_code = """
        namespace HelloWorld
        {
            class Program
            {
                public static void Main(string[] args)
                {
                    Console.WriteLine(5+8);
                    

                }
            }
        }


                       """
    st.code(csharp_code, language='csharp')


def solation1():
    st.subheader("תרגיל ראשון ")
    csharp_code = """
            namespace HelloWorld
            {
                class Program
                {
                    public static void Main(string[] args)
                    {
                        Console.WriteLine("Hello My name is Eli ");


                    }
                }
            }


                           """
    st.code(csharp_code, language='csharp')


def solation2():
    st.subheader("תרגיל שני ")
    csharp_code = """
            
namespace HelloWorld
{
    class Program
    {
        public static void Main(string[] args)
        {
            int num1 = 50;
            int num2 = 70;
            int num3 = 60;
            int num4 = 75;
            int num5 = 90;
            int sum = num1 + num2 + num3 + num4 + num5;
            double avg =  sum / 5;
            Console.WriteLine("is average is "+avg);

        }
    }
}




                           """
    st.code(csharp_code, language='csharp')
