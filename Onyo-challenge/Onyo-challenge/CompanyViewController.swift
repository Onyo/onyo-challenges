//
//  CompanyViewController.swift
//  Onyo-challenge
//
//  Created by Matheus Cavalca on 5/13/16.
//  Copyright © 2016 Matheus Cavalca. All rights reserved.
//

import UIKit
import MapKit
import RealmSwift

class CompanyViewController: UIViewController {

    // MARK: - Properties
    
    @IBOutlet var tableView: UITableView!
    
    var companies = [Company]()
    
    var destinationCategoriesViewController: CategoryViewController?
    
    lazy var refreshControl: UIRefreshControl = {
        let refresh = UIRefreshControl()
        refresh.addTarget(self, action: #selector(CompanyViewController.refreshTableViewData), forControlEvents: UIControlEvents.ValueChanged)
        return refresh
    }()
    
    // MARK: - Life Cycle
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        configContent()
        fetchCompanyList(nil)
    }
    
    override func viewDidAppear(animated: Bool) {
        super.viewDidAppear(animated)
        
        configWithRealmData()
        destinationCategoriesViewController = nil
    }
    
    // MARK: - Configuration
    
    func configContent() {
        tableView.rowHeight = UITableViewAutomaticDimension
        tableView.estimatedRowHeight = 220.0
        tableView.addSubview(refreshControl)
        
        navigationItem.config()
    }
    
    func configWithRealmData() {
        companies = Company.companiesFromRealm()
        sortCompaniesByLocation(companies)
        tableView.reloadData()
    }
    
    // MARK: - API handlers
    
    func fetchCompanyList(completion: (() -> Void)?) {
        OnyoAPIManager.sharedInstance.fetchCompanyList({ (companies, categories) in
           self.deleteAllRealm()
            
            self.companies = companies
            for company in companies {
                company.save()
            }
            
            for category in categories {
                category.save()
            }
            
            if let destination = self.destinationCategoriesViewController {
                destination.loadCategories()
            }
        
            self.sortCompaniesByLocation(companies)
            self.tableView.reloadData()
            completion?()
        }) { (error) in
        }
    }
    
    func deleteAllRealm() {
        let realm = try! Realm()
        realm.beginWrite()
        realm.deleteAll()
        try! realm.commitWrite()
    }
    
    // MARK: - Action
    
    func refreshTableViewData() {
        tableView.scrollEnabled = false
        fetchCompanyList() { () -> Void in
            NSTimer.scheduledTimerWithTimeInterval(0.5, target: self, selector: #selector(CompanyViewController.endRefreshing), userInfo: nil, repeats: false)
        }
    }
    
    func endRefreshing() {
        self.refreshControl.endRefreshing()
        self.tableView.scrollEnabled = true
    }
    
    func sortCompaniesByLocation(companies: [Company]) {
        if let userLocation = LocationManager.sharedInstance.currentLocation {
            self.companies = companies.sort({ ($0.location?.distanceFromLocation(userLocation)) < ($1.location?.distanceFromLocation(userLocation)) })
        }
    }
    
    // MARK: - Navigation
    
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        if segue.identifier == "CategoriesSegue" {
            let destinationBar = segue.destinationViewController as! UITabBarController
            let destination = destinationBar.viewControllers![TabIndexes.CategoriesIndex.rawValue] as! CategoryViewController
            destinationCategoriesViewController = destination
        }
    }
}

extension CompanyViewController: UITableViewDataSource {
    
    func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return companies.count
    }
    
    func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        let cellIdentifier = NibObjects.reuseIdentifierFor(.CompanyTableViewCell)
        let cell = tableView.dequeueReusableCellWithIdentifier(cellIdentifier, forIndexPath: indexPath) as! CompanyTableViewCell
        
        let company = companies[indexPath.row]
        
        let openMap: () -> Void = { () in
            if let latitude = company.addressLatitude.value, let longitude = company.addressLongitude.value {
                let placemark = MKPlacemark(coordinate: CLLocation(latitude: latitude, longitude: longitude).coordinate, addressDictionary: nil)
                let item = MKMapItem(placemark: placemark)
                item.name = company.displayName
                item.openInMapsWithLaunchOptions(nil)
            }
        }
        
        cell.configureCellWith(company, indexPath: indexPath, openMap: openMap)

        return cell
    }
    
    func tableView(tableView: UITableView, heightForRowAtIndexPath indexPath: NSIndexPath) -> CGFloat {
        return UITableViewAutomaticDimension
    }
    
}

extension CompanyViewController: UITableViewDelegate {
    
    func tableView(tableView: UITableView, didSelectRowAtIndexPath indexPath: NSIndexPath) {
        performSegueWithIdentifier("CategoriesSegue", sender: self)
    }
    
}