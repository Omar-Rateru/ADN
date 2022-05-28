public class CalculatriceSimple {
	public static void main (String[] args) {
		try {
		Nombre six = new Nombre(8);
		Nombre dix = new Nombre(15);
		Nombre zero = new Nombre(0);
		
		Operation s1 = new Multiplication(dix, six);
		System.out.println(s1 + "=" + s1.valeur());
		
		Operation s2 = new Addition(dix, six);
		System.out.println(s2 + "=" + s2.valeur());
		
		Operation s3 = new Soustraction(dix, six);
		System.out.println(s3 + "=" + s3.valeur());
		
		Operation s4 = new Division(dix, six);
		System.out.println(s4 + "=" + s4.valeur());
		
		
		System.out.println(s1);
		System.out.println(s2);
		System.out.println(s3);
		System.out.println(s4);


		Operation s5 = new Division(dix, zero);
		System.out.println(s5 + "=" + s5.valeur());
	}
	        catch (Exception e){System.err.println(e.getMessage());}
}
}
