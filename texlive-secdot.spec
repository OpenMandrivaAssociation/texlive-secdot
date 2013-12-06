# revision 20208
# category Package
# catalog-ctan /macros/latex/contrib/secdot
# catalog-date 2010-10-17 10:06:32 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-secdot
Version:	1.0
Release:	5
Summary:	Section numbers with trailing dots
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/secdot
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/secdot.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/secdot.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Makes the numbers of \section commands come out with a trailing
dot. Includes a command whereby the same can be made to happen
with other sectioning commands.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/secdot/secdot.sty
%doc %{_texmfdistdir}/doc/latex/secdot/secdot.ltx
%doc %{_texmfdistdir}/doc/latex/secdot/secdot.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 755859
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 719496
- texlive-secdot
- texlive-secdot
- texlive-secdot
- texlive-secdot

