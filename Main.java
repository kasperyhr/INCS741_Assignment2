// "static void main" must be defined in a public class.

public class Main {
    public static void main(String[] args) {
        Main main = new Main();
        String encryptionString = "CRYPTOLOGY IS THE PRACTICE AND STUDY OF TECHNIQUES FOR SECURE COMMUNICATION IN THE PRESENCE OF THIRD PARTIES CALLED ADVERSARIES.";
        // String decryptionString = "TAOTINEN KAT I ODIOAEI OHHLSCTE TTETOEL BI IHI GAO   EPSEA TO SS  EEK  ELRCPTSIY EANRPHMCYEK E CREAAIEJURTE  IEASHI MA DRN RH  AUWTA RF EFTFHENTPSF Q   TAILB E TTECAPMSIYIY SRPURNTBL YCL OANAO  E  TVREAOSHOTTNULSRHK";
       String decryptionString = "TPSNIONFRMHANOIREEOIBTSEAKLAPSEHISOBPEGTBRQREPTTMHRTHTTAWEAACTFVAECAOLHANSEEKFHALOITUEEAICNLEYOLTOLEPADFKATATSJMSIINSHROCTITRIEEAKYNHYUEOTTSTATSIIRSARERUYUEDPCLETEROINEIYEHC";
        System.out.println(main.encryption(encryptionString, 4, 5));
        // System.out.println(main.decryption(decryptionString, 3, 3));
    }
    
    public String sanitize(String str) {
        StringBuffer sb = new StringBuffer();
        for (char ch: str.toCharArray()) {
            char c = Character.toLowerCase(ch);
            
            if (c < 'a' || c > 'z') {
                continue;
            }
            
            sb.append(c);
        }
        
        return sb.toString();
    }
    
    
    public String encryption(String str, int rails, int rounds) {
        str = sanitize(str);
        while (rounds > 0) {
            rounds--;
            StringBuffer[] sbs = new StringBuffer[rails];
            for (int i = 0; i < rails; i++) {
                sbs[i] = new StringBuffer();
            }
            
            int index = 0;
            boolean addIndex = true;
            for (int i = 0; i < str.length(); i++) {
                sbs[index].append(str.charAt(i));
                if (index == 0) {
                    addIndex = true;
                }
                if (index == rails - 1) {
                    addIndex = false;
                }
                
                index += addIndex ? 1 : -1;
            }
            
            str = "";
            for (int i = 0; i < rails; i++) {
                str += sbs[i].toString();
            }
        }
        
        return str;
    }
    
    public String decryption(String str, int rails, int rounds) {
        str = sanitize(str);
        while (rounds > 0) {
            rounds--;
            int[] lens = new int[rails];
            
            int index = 0;
            boolean addIndex = true;
            for (char ch: str.toCharArray()) {
                lens[index]++;
                
                if (index == 0) {
                    addIndex = true;
                }
                if (index == rails - 1) {
                    addIndex = false;
                }
                
                index += addIndex ? 1 : -1;
            }
            
            String[] strs = new String[rails];
            index = 0;
            for (int i = 0; i < rails; i++) {
                strs[i] = str.substring(index, index + lens[i]);
                index = index + lens[i];
            }
            
            Arrays.fill(lens, 0);
            StringBuffer sb = new StringBuffer();
            index = 0;
            addIndex = true;
            
            for (int i = 0; i < str.length(); i++) {
                sb.append(strs[index].charAt(lens[index]++));
                
                if (index == 0) {
                    addIndex = true;
                }
                if (index == rails - 1) {
                    addIndex = false;
                }
                
                index += addIndex ? 1 : -1;
            }
            str = sb.toString();
        }
        
        return str;
    }
}
