// Define an interface named IMyInterface.
namespace DefineIMyInterface
{
    using System;

    public interface IMyInterface
    {
        // Any class that implements IMyInterface must define a method
        // that matches the following signature.
        void MethodB();
    }
}


// Define extension methods for IMyInterface.
namespace Extensions
{
    using System;
    using DefineIMyInterface;

    // The following extension methods can be accessed by instances of any 
    // class that implements IMyInterface.
    public static class Extension
    {
        public static void MethodA(this IMyInterface myInterface, int i)
        {
            Console.WriteLine
                ("Extension.MethodA(this IMyInterface myInterface, int i)");
        }

        public static void MethodA(this IMyInterface myInterface, string s)
        {
            Console.WriteLine
                ("Extension.MethodA(this IMyInterface myInterface, string s)");
        }

        // This method is never called in ExtensionMethodsDemo1, because each 
        // of the three classes A, B, and C implements a method named MethodB
        // that has a matching signature.
        public static void MethodB(this IMyInterface myInterface)
        {
            Console.WriteLine
                ("Extension.MethodB(this IMyInterface myInterface)");
        }
    }
}


// Define three classes that implement IMyInterface, and then use them to test
// the extension methods.
namespace ExtensionMethodsDemo1
{
    using System;
    using Extensions;
    using DefineIMyInterface;
   
    class A : IMyInterface
    {
        public void MethodB() { Console.WriteLine("A.MethodB()"); }
    }

    class B : IMyInterface
    {
        public void MethodB() { Console.WriteLine("B.MethodB()"); }
        public void MethodA(int i) { Console.WriteLine("B.MethodA(int i)"); }
    }

    class C : IMyInterface
    {
        public void MethodB() { Console.WriteLine("C.MethodB()"); }
        public void MethodA(object obj)
        {
            Console.WriteLine("C.MethodA(object obj)");
        }
        public void MethodA(int i) { Console.WriteLine("C.MethodA(int i)"); }
    }

    class ExtMethodDemo
    {
        static void Main(string[] args)
        {
            // Declare an instance of class A, class B, and class C.
            A a = new A();
            B b = new B();
            C c = new C();

            // For a, b, and c, call the following methods:
            //      -- MethodA with an int argument
            //      -- MethodA with a string argument
            //      -- MethodB with no argument.

            // A contains no MethodA, so each call to MethodA resolves to 
            // the extension method that has a matching signature.
            a.MethodA(1);           // Extension.MethodA(object, int)
            a.MethodA("hello");     // Extension.MethodA(object, string)

            // A has a method that matches the signature of the following call
            // to MethodB.
            a.MethodB();            // A.MethodB()

            // B has methods that match the signatures of the following
            // method calls.
            b.MethodA(1);           // B.MethodA(int)
            b.MethodB();            // B.MethodB()

            // B has no matching method for the following call, but 
            // class Extension does.
            b.MethodA("hello");     // Extension.MethodA(object, string)

            // C contains an instance method that matches each of the following
            // method calls.
            c.MethodA(1);           // C.MethodA(object)
            c.MethodA("hello");     // C.MethodA(object)
            c.MethodB();            // C.MethodB()

            Console.ReadKey();

           
        }
    }
}
/* Output:
    Extension.MethodA(this IMyInterface myInterface, int i)
    Extension.MethodA(this IMyInterface myInterface, string s)
    A.MethodB()
    B.MethodA(int i)
    B.MethodB()
    Extension.MethodA(this IMyInterface myInterface, string s)
    C.MethodA(object obj)
    C.MethodA(object obj)
    C.MethodB()
 */







namespace ConsoleApplication5
{

    public interface IHuman
    {
        int Age
        { get; set; }

        string GetSurName();
    }

    [Serializable]
    public class Woman : IHuman, IComparable, IDisposable
    {
        public string Name { get; set; }

        private int age;
        private string surname;

        public Woman(string surname)
        {
            this.age = 10;
            this.surname = surname;
        }

        public Woman() : this("Default") { }

        [XmlIgnore]
        public int Age
        {
            get { return this.age; }
            set { this.age = value; }
        }

        public string GetSurName()
        {
            return this.surname;
        }

        int IComparable.CompareTo(object o)
        {
            if (!(o is Woman))
                throw new ArgumentException();

            Woman w = (Woman)o;

            if (this.age > w.age) return 1;
            if (this.age < w.age) return -1;
            else return 0;
        }

        public void Dispose()
        {
            GC.SuppressFinalize(this);
        }
    }


    public class Women : IEnumerable, IEnumerator, IDisposable
    {
        Woman[] women;
        int pos = -1;

        public Woman this[string name]
        {
            get
            {
                foreach (Woman w in women)
                {
                    if (w.GetSurName() == name) return w;
                }
                return null;
            }

            set { this[name] = value; }
        }

        public Woman this[int index]
        {
            get { return (Woman)women[index]; }
            set { women[index] = value; }
        }

        public IEnumerator GetEnumerator() { return (IEnumerator)this; }
        public bool MoveNext()
        {
            if (pos < women.Length - 1)
            {
                pos++;
                return true;
            }
            else
                return false;
        }

        public void Reset()
        {
            pos = -1;
        }

        public object Current
        {
            get { return women[pos]; }
        }

        public Women(int n)
        {
            women = new Woman[n];
            for (int i = 0; i < n; i++)
            {
                women[i] = new Woman("Woman #" + i.ToString());
                women[i].Age = n - i;
                Console.WriteLine("{0} woman is {1} , {2} years ", i, women[i].GetSurName(), women[i].Age);
            }
        }

        public void Sort()
        {
            Array.Sort(this.women);
            this.Reset();
        }

        public void Dispose()
        {
            foreach (Woman w in women)
                w.Dispose();
        }

        ~Women()
        {
            Dispose();
        }
    }



    class Program
    {
        static void Main0(string[] args)
        {
            Women ws = new Women(5);


            foreach (Woman w in ws)
            {
                Console.WriteLine(w.GetSurName());
            }

            ws.Sort();

            Console.WriteLine("-----------");

            foreach (Woman w in ws)
            {
                Console.WriteLine(w.GetSurName());
            }

            /* Object obj = new Object();
             WeakReference wr = new WeakReference(obj);
             obj = null;
             GC.Collect();
             obj = (Object)wr.Target;
             if (obj != null)
                 Console.WriteLine("Object isn't collected");
             else
                 Console.WriteLine("Object is already collected");
                 */

            XmlSerializer serializer = new XmlSerializer(typeof(Woman));
            string xml;
            using (StringWriter stringWriter = new StringWriter())
            {
                Woman w = new Woman() { Name = "Alice", Age = 20 };
                serializer.Serialize(stringWriter, w);
                xml = stringWriter.ToString();
            }

            Console.WriteLine(xml);

            using (StringReader stringReader = new StringReader(xml))
            {
                Woman w = (Woman)serializer.Deserialize(stringReader);
                Console.WriteLine("{0} is {1} years old", w.Name, w.Age);
            }



            Console.ReadKey();
        }
    }
}

/*
 XML serializer - doesn't have the highest performance, can't work with private fields
if XML serializer can't find a specific field, it won't throw any exception, it'll just set the property to its default value     
     
     */
